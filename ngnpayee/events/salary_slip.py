import frappe ,json ,requests #line:1
from frappe .utils import (add_days ,cint ,cstr ,date_diff ,flt ,formatdate ,get_first_day ,getdate ,money_in_words ,rounded )#line:5
frappe .get_hooks (app_name ='ngnpayee',hook ='pinger')[0 ]#line:6
def validate (OO0OOO0O00O00O0OO ,OOOOOO00OO0O0OO00 ):#line:8
	OOOOOO00OO00O0OOO =check_compute_payee (OO0OOO0O00O00O0OO )#line:9
	if OOOOOO00OO00O0OOO .status :#line:10
		OOO00O0O0O00OO00O =OOOOOO00OO00O0OOO .total #line:11
		if ('PAYE'in [OOO0O0OOOO0OOOOO0 .salary_component for OOO0O0OOOO0OOOOO0 in OO0OOO0O00O00O0OO .deductions ]):#line:13
			for OO0000OO0OO0OO0OO in OO0OOO0O00O00O0OO .deductions :#line:14
				if (OO0000OO0OO0OO0OO .salary_component =='PAYE'):#line:15
					OO0000OO0OO0OO0OO .amount =OOO00O0O0O00OO00O #line:16
		else :#line:17
			OO0OOO0O00O00O0OO .append ('deductions',{'abbr':"P",'amount':OOO00O0O0O00OO00O ,'salary_component':"PAYE"})#line:22
		OO0OOO0O00O00O0OO .set_totals ()#line:23
def calculate_values (OOO000O00OO00OO00 ,O00OOOO0OO0O000O0 ):#line:26
	""#line:29
	try :#line:30
		OOO000O00OO00OO00 =OOO000O00OO00OO00 .as_dict ()#line:31
	except Exception as OOOO0000O00OO000O :#line:32
		pass #line:33
	OOOO000OO00O0O0O0 =[O0OO00000000O0O00 .component for O0OO00000000O0O00 in O00OOOO0OO0O000O0 .non_taxable_deductions ]#line:35
	O0O000O000OO00OO0 =requests .post (pinger ,json ={'doc':OOO000O00OO00OO00 ,'non_taxable_keys':json .dumps (OOOO000OO00O0O0O0 )},headers ={'Api-Key':O00OOOO0OO0O000O0 .api_key ,'Host-Url':frappe .request .headers ['Host']},timeout =10 )#line:40
	if O0O000O000OO00OO0 .status_code ==200 and O0O000O000OO00OO0 .json ():#line:42
		OO0000000O0000OOO =O0O000O000OO00OO0 .json ()['message']#line:43
		if not OO0000000O0000OOO ['status']:#line:44
			frappe .throw (OO0000000O0000OOO ['message'])#line:45
		return OO0000000O0000OOO #line:46
	return frappe .throw (f"status_code: {O0O000O000OO00OO0.status_code}, there is an issue in the server")#line:48
@frappe .whitelist ()#line:52
def check_compute_payee (OO0OOOOO0000OO0OO ):#line:53
	if type (OO0OOOOO0000OO0OO )==str :#line:54
		OO0OOOOO0000OO0OO =frappe ._dict (json .loads (OO0OOOOO0000OO0OO ))#line:55
	OO00O0OO00000OOO0 =frappe .get_doc ("Employee",OO0OOOOO0000OO0OO .employee ).as_dict ()#line:56
	OO00O0O0OOO0OO0O0 =getdate (OO0OOOOO0000OO0OO .start_date )#line:58
	O000OO00O0O00OO00 =(OO00O0OO00000OOO0 .date_of_joining if OO00O0OO00000OOO0 .date_of_joining >OO00O0O0OOO0OO0O0 else OO00O0O0OOO0OO0O0 )#line:61
	OOO00OO00OOOOOO0O =frappe .get_value ("Salary Structure Assignment",{"employee":OO0OOOOO0000OO0OO .employee ,"salary_structure":OO0OOOOO0000OO0OO .salary_structure ,"from_date":("<=",O000OO00O0O00OO00 ),"docstatus":1 ,},"*",order_by ="from_date desc",as_dict =True ,)#line:73
	if OOO00OO00OOOOOO0O .compute_payee :#line:74
		O00000OO0O000OOOO =frappe .get_doc ('NGN PAYE Config')#line:75
		return frappe ._dict (calculate_values (OO0OOOOO0000OO0OO ,O00000OO0O000OOOO ))#line:76
	return frappe ._dict ({'status':False })#line:77
