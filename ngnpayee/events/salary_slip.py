import frappe ,json ,requests #line:1
from frappe .utils import (add_days ,cint ,cstr ,date_diff ,flt ,formatdate ,get_first_day ,getdate ,money_in_words ,rounded )#line:5
pinger =frappe .get_hooks ('pinger')#line:6
def validate (OO0O0OOOO0O0O0O00 ,OOOO00000OOOO000O ):#line:8
	O0O00OOO0OO0OOO0O =check_compute_payee (OO0O0OOOO0O0O0O00 )#line:9
	if O0O00OOO0OO0OOO0O .status :#line:10
		OO000000O00O0OOO0 =O0O00OOO0OO0OOO0O .total #line:11
		if ('PAYE'in [O0O0OO0O0OO000OO0 .salary_component for O0O0OO0O0OO000OO0 in OO0O0OOOO0O0O0O00 .deductions ]):#line:13
			for O0OOO0O0O0O0O0O0O in OO0O0OOOO0O0O0O00 .deductions :#line:14
				if (O0OOO0O0O0O0O0O0O .salary_component =='PAYE'):#line:15
					O0OOO0O0O0O0O0O0O .amount =OO000000O00O0OOO0 #line:16
		else :#line:17
			OO0O0OOOO0O0O0O00 .append ('deductions',{'abbr':"P",'amount':OO000000O00O0OOO0 ,'salary_component':"PAYE"})#line:22
		OO0O0OOOO0O0O0O00 .set_totals ()#line:23
def calculate_values (OO00O00OO00000O00 ,OOO0OOO0OO0000O00 ):#line:26
	""#line:29
	try :#line:30
		OO00O00OO00000O00 =OO00O00OO00000O00 .as_dict ()#line:31
	except Exception as OOO00000O00000OOO :#line:32
		pass #line:33
	OOOO0O0O0O00O0OOO =[OOOOOO0O0OOO00000 .component for OOOOOO0O0OOO00000 in OOO0OOO0OO0000O00 .non_taxable_deductions ]#line:35
	OO00OOOO0O00O0OOO =requests .post (pinger ,json ={'doc':OO00O00OO00000O00 ,'non_taxable_keys':json .dumps (OOOO0O0O0O00O0OOO )},headers ={'Api-Key':OOO0OOO0OO0000O00 .api_key ,'Host-Url':frappe .request .headers ['Host']},timeout =10 )#line:40
	if OO00OOOO0O00O0OOO .status_code ==200 and OO00OOOO0O00O0OOO .json ():#line:42
		O00OO00O000O00O00 =OO00OOOO0O00O0OOO .json ()['message']#line:43
		if not O00OO00O000O00O00 ['status']:#line:44
			frappe .throw (O00OO00O000O00O00 ['message'])#line:45
		return O00OO00O000O00O00 #line:46
	return frappe .throw (f"status_code: {OO00OOOO0O00O0OOO.status_code}, there is an issue in the server")#line:48
@frappe .whitelist ()#line:52
def check_compute_payee (O0OOO000O0000O0OO ):#line:53
	if type (O0OOO000O0000O0OO )==str :#line:54
		O0OOO000O0000O0OO =frappe ._dict (json .loads (O0OOO000O0000O0OO ))#line:55
	OOOO0000OO000000O =frappe .get_doc ("Employee",O0OOO000O0000O0OO .employee ).as_dict ()#line:56
	OOOOO000O0OO0O000 =getdate (O0OOO000O0000O0OO .start_date )#line:58
	OO000OOOO0O00OOOO =(OOOO0000OO000000O .date_of_joining if OOOO0000OO000000O .date_of_joining >OOOOO000O0OO0O000 else OOOOO000O0OO0O000 )#line:61
	O0OOOO00O0OOOO00O =frappe .get_value ("Salary Structure Assignment",{"employee":O0OOO000O0000O0OO .employee ,"salary_structure":O0OOO000O0000O0OO .salary_structure ,"from_date":("<=",OO000OOOO0O00OOOO ),"docstatus":1 ,},"*",order_by ="from_date desc",as_dict =True ,)#line:73
	if O0OOOO00O0OOOO00O .compute_payee :#line:74
		OO0O00O000OO0O00O =frappe .get_doc ('NGN PAYE Config')#line:75
		return frappe ._dict (calculate_values (O0OOO000O0000O0OO ,OO0O00O000OO0O00O ))#line:76
	return frappe ._dict ({'status':False })#line:77
