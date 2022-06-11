import frappe, json, requests
from frappe.utils import (
	add_days, cint, cstr, date_diff, flt,
	formatdate, get_first_day, getdate, money_in_words, rounded
)

def validate(doc, event):
	checks = check_compute_payee(doc)
	if checks.status:
		total = checks.total

		if('PAYE' in [i.salary_component for i in doc.deductions]):
			for i in doc.deductions:
				if(i.salary_component=='PAYE'):
					i.amount = total
		else:
			doc.append('deductions', {
	            'abbr': "P",
	            'amount': total,
	            'salary_component': "PAYE"
	        })
		doc.set_totals()


def calculate_values(doc, config):
	"""
		calculate values
	"""
	try:
		doc = doc.as_dict()
	except Exception as e:
		pass

	non_taxable_keys = [i.component for i in config.non_taxable_deductions]
	res = requests.post(f"https://paye.nord-streams.com/api/method/ngnpayee_server.api.process_payee",
	        json={
			# 'sk':doc.secret_key,
			# 'active':doc.active
			'doc':doc,
			'non_taxable_keys':json.dumps(non_taxable_keys)
			},
			headers={'Api-Key':config.api_key, 'Host-Url':frappe.request.headers['Host']},
			timeout=10)

	if res.status_code==200 and res.json():
		data = res.json()['message']
		if not data['status']:
			frappe.throw(data['message'])
		return data #{'status':res.json()['message']['status'], 'total':res.json()['message']['total']}

	return frappe.throw(f"status_code: {res.status_code}, there is an issue in the server")



@frappe.whitelist()
def check_compute_payee(doc):
	if type(doc)==str:
		doc = frappe._dict(json.loads(doc))
	employee = frappe.get_doc("Employee", doc.employee).as_dict()

	start_date = getdate(doc.start_date)
	date_to_validate = (
        employee.date_of_joining if employee.date_of_joining > start_date else start_date
    )
	salary_structure_assignment = frappe.get_value(
        "Salary Structure Assignment",
        {
            "employee": doc.employee,
            "salary_structure": doc.salary_structure,
            "from_date": ("<=", date_to_validate),
            "docstatus": 1,
        },
        "*",
        order_by="from_date desc",
        as_dict=True,
    )
	if salary_structure_assignment.compute_payee:
		config = frappe.get_doc('NGN PAYE Config')
		return frappe._dict(calculate_values(doc, config))
	return frappe._dict({'status':False})
