import frappe ,json ,requests #line:1
from frappe .utils import (add_days ,cint ,cstr ,date_diff ,flt ,formatdate ,get_first_day ,getdate ,money_in_words ,rounded )#line:5
pinger =frappe .get_hooks (app_name ='ngnpayee',hook ='pinger')[0 ]#line:6
def validate (OOO000OOOO0OOO000 ,OO00O0O000OOOO00O ):#line:8
	O00O000O0OOOO0OO0 =check_compute_payee (OOO000OOOO0OOO000 )#line:9
	if O00O000O0OOOO0OO0 .status :#line:10
		OOOOOOOOOO0OO0OOO =O00O000O0OOOO0OO0 .total #line:11
		if ('PAYE'in [O0OO0O0OO0O0O0OOO .salary_component for O0OO0O0OO0O0O0OOO in OOO000OOOO0OOO000 .deductions ]):#line:13
			for O0O00000000OO000O in OOO000OOOO0OOO000 .deductions :#line:14
				if (O0O00000000OO000O .salary_component =='PAYE'):#line:15
					O0O00000000OO000O .amount =OOOOOOOOOO0OO0OOO #line:16
		else :#line:17
			OOO000OOOO0OOO000 .append ('deductions',{'abbr':"P",'amount':OOOOOOOOOO0OO0OOO ,'salary_component':"PAYE"})#line:22
		OOO000OOOO0OOO000 .set_totals ()#line:23
def calculate_values (OOOOOO00000O000O0 ,OOOOO0O0O00O00O0O ):#line:26
	""#line:29
	try :#line:30
		OOOOOO00000O000O0 =OOOOOO00000O000O0 .as_dict ()#line:31
	except Exception as O0000000OOOOO0O00 :#line:32
		pass #line:33
	OOO00OO00OOO00OO0 =[OOOOOO00OO00OO000 .component for OOOOOO00OO00OO000 in OOOOO0O0O00O00O0O .non_taxable_deductions ]#line:35
	OO0O000O00O0000O0 =requests .post (pinger ,json ={'doc':OOOOOO00000O000O0 ,'non_taxable_keys':json .dumps (OOO00OO00OOO00OO0 )},headers ={'Api-Key':OOOOO0O0O00O00O0O .api_key ,'Host-Url':frappe .request .headers ['Host']},timeout =10 )#line:40
	if OO0O000O00O0000O0 .status_code ==200 and OO0O000O00O0000O0 .json ():#line:42
		OOOO000OOOOO0O00O =OO0O000O00O0000O0 .json ()['message']#line:43
		if not OOOO000OOOOO0O00O ['status']:#line:44
			frappe .throw (OOOO000OOOOO0O00O ['message'])#line:45
		return OOOO000OOOOO0O00O #line:46
	return frappe .throw (f"status_code: {OO0O000O00O0000O0.status_code}, there is an issue in the server")#line:48
@frappe .whitelist ()#line:52
def check_compute_payee (OO000O00OOO00OOOO ):#line:53
	if type (OO000O00OOO00OOOO )==str :#line:55
		OO000O00OOO00OOOO =frappe ._dict (json .loads (OO000O00OOO00OOOO ))#line:56
	OO0000O0O0OO0OOO0 =frappe .get_doc ("Employee",OO000O00OOO00OOOO .employee ).as_dict ()#line:57
	O0O00OO00000O0OOO =getdate (OO000O00OOO00OOOO .start_date )#line:59
	OO00OO0O000OOOOOO =(OO0000O0O0OO0OOO0 .date_of_joining if OO0000O0O0OO0OOO0 .date_of_joining >O0O00OO00000O0OOO else O0O00OO00000O0OOO )#line:62
	OOOOOO0OOOO0OOOO0 =frappe .get_value ("Salary Structure Assignment",{"employee":OO000O00OOO00OOOO .employee ,"salary_structure":OO000O00OOO00OOOO .salary_structure ,"from_date":("<=",OO00OO0O000OOOOOO ),"docstatus":1 ,},"*",order_by ="from_date desc",as_dict =True ,)#line:74
	if OOOOOO0OOOO0OOOO0 .compute_payee :#line:75
		O000OOOOO00O00O00 =frappe .get_doc ('NGN PAYE Config')#line:76
		return frappe ._dict (calculate_values (OO000O00OOO00OOOO ,O000OOOOO00O00O00 ))#line:77
	return frappe ._dict ({'status':False })#line:78
