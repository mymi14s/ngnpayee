import frappe ,json ,requests #line:1
from frappe .utils import (add_days ,cint ,cstr ,date_diff ,flt ,formatdate ,get_first_day ,getdate ,money_in_words ,rounded )#line:5
pinger =frappe .get_hooks ('pinger')#line:6
def validate (OOOO000000OOOOOO0 ,O0O00OO0O0OOOOOO0 ):#line:8
	O00000OOOO0OO00OO =check_compute_payee (OOOO000000OOOOOO0 )#line:9
	if O00000OOOO0OO00OO .status :#line:10
		O0O0OO00OO0000OO0 =O00000OOOO0OO00OO .total #line:11
		if ('PAYE'in [OOOO0OOOO000000OO .salary_component for OOOO0OOOO000000OO in OOOO000000OOOOOO0 .deductions ]):#line:13
			for OO0O0O00O0OO000O0 in OOOO000000OOOOOO0 .deductions :#line:14
				if (OO0O0O00O0OO000O0 .salary_component =='PAYE'):#line:15
					OO0O0O00O0OO000O0 .amount =O0O0OO00OO0000OO0 #line:16
		else :#line:17
			OOOO000000OOOOOO0 .append ('deductions',{'abbr':"P",'amount':O0O0OO00OO0000OO0 ,'salary_component':"PAYE"})#line:22
		OOOO000000OOOOOO0 .set_totals ()#line:23
def calculate_values (OOOO000OOO00O0OOO ,O0O00000O000OOOOO ):#line:26
	""#line:29
	try :#line:30
		OOOO000OOO00O0OOO =OOOO000OOO00O0OOO .as_dict ()#line:31
	except Exception as O000O0O0000OO0O0O :#line:32
		pass #line:33
	OO0OO000O0000O000 =[O0O0O0O00O00O00OO .component for O0O0O0O00O00O00OO in O0O00000O000OOOOO .non_taxable_deductions ]#line:35
	OOO000OO0O0O0OOO0 =requests .post (pinger ,json ={'doc':OOOO000OOO00O0OOO ,'non_taxable_keys':json .dumps (OO0OO000O0000O000 )},headers ={'Api-Key':O0O00000O000OOOOO .api_key ,'Host-Url':frappe .request .headers ['Host']},timeout =10 )#line:40
	if OOO000OO0O0O0OOO0 .status_code ==200 and OOO000OO0O0O0OOO0 .json ():#line:42
		OOO000OO0OO0OO0O0 =OOO000OO0O0O0OOO0 .json ()['message']#line:43
		if not OOO000OO0OO0OO0O0 ['status']:#line:44
			frappe .throw (OOO000OO0OO0OO0O0 ['message'])#line:45
		return OOO000OO0OO0OO0O0 #line:46
	return frappe .throw (f"status_code: {OOO000OO0O0O0OOO0.status_code}, there is an issue in the server")#line:48
@frappe .whitelist ()#line:52
def check_compute_payee (O000O00OOO000OO00 ):#line:53
	if type (O000O00OOO000OO00 )==str :#line:54
		O000O00OOO000OO00 =frappe ._dict (json .loads (O000O00OOO000OO00 ))#line:55
	OOOOOOOOOOOOO0000 =frappe .get_doc ("Employee",O000O00OOO000OO00 .employee ).as_dict ()#line:56
	OOOO00O0O00OOO00O =getdate (O000O00OOO000OO00 .start_date )#line:58
	OO0O00000O000O000 =(OOOOOOOOOOOOO0000 .date_of_joining if OOOOOOOOOOOOO0000 .date_of_joining >OOOO00O0O00OOO00O else OOOO00O0O00OOO00O )#line:61
	O000O00O0000OOO0O =frappe .get_value ("Salary Structure Assignment",{"employee":O000O00OOO000OO00 .employee ,"salary_structure":O000O00OOO000OO00 .salary_structure ,"from_date":("<=",OO0O00000O000O000 ),"docstatus":1 ,},"*",order_by ="from_date desc",as_dict =True ,)#line:73
	if O000O00O0000OOO0O .compute_payee :#line:74
		OOO00OOOOO0O0OOO0 =frappe .get_doc ('NGN PAYE Config')#line:75
		return frappe ._dict (calculate_values (O000O00OOO000OO00 ,OOO00OOOOO0O0OOO0 ))#line:76
	return frappe ._dict ({'status':False })#line:77
