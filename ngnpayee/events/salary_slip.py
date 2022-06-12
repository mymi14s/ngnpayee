import frappe ,json ,requests #line:1
from frappe .utils import (add_days ,cint ,cstr ,date_diff ,flt ,formatdate ,get_first_day ,getdate ,money_in_words ,rounded )#line:5
pinger =frappe .get_hooks (app_name ='ngnpayee',hook ='pinger')[0 ]#line:6
def validate (O00O000OO0000O00O ,O0OOO0OOO00OO0000 ):#line:8
	O0OO000OO0O000O0O =check_compute_payee (O00O000OO0000O00O )#line:9
	if O0OO000OO0O000O0O .status :#line:10
		O000O00OO000OOO00 =O0OO000OO0O000O0O .total #line:11
		if ('PAYE'in [O0OO0O00OOOOO0O0O .salary_component for O0OO0O00OOOOO0O0O in O00O000OO0000O00O .deductions ]):#line:13
			for O00000O0000OOOOO0 in O00O000OO0000O00O .deductions :#line:14
				if (O00000O0000OOOOO0 .salary_component =='PAYE'):#line:15
					O00000O0000OOOOO0 .amount =O000O00OO000OOO00 #line:16
		else :#line:17
			O00O000OO0000O00O .append ('deductions',{'abbr':"P",'amount':O000O00OO000OOO00 ,'salary_component':"PAYE"})#line:22
		O00O000OO0000O00O .set_totals ()#line:23
def calculate_values (OOOOOO000OOO0OOO0 ,OO000O0O00OOOO0OO ):#line:26
	""#line:29
	try :#line:30
		OOOOOO000OOO0OOO0 =OOOOOO000OOO0OOO0 .as_dict ()#line:31
	except Exception as OOOOO0OO00OO00OOO :#line:32
		pass #line:33
	OOOO0OOOOO0OOOOO0 =[OO000OO0O00O00O0O .component for OO000OO0O00O00O0O in OO000O0O00OOOO0OO .non_taxable_deductions ]#line:35
	OO000OOO00O0OO00O =requests .post (pinger ,json ={'doc':OOOOOO000OOO0OOO0 ,'non_taxable_keys':json .dumps (OOOO0OOOOO0OOOOO0 )},headers ={'Api-Key':OO000O0O00OOOO0OO .api_key ,'Host-Url':frappe .request .headers ['Host']},timeout =10 )#line:40
	if OO000OOO00O0OO00O .status_code ==200 and OO000OOO00O0OO00O .json ():#line:42
		O00OOO00OOOOO0O00 =OO000OOO00O0OO00O .json ()['message']#line:43
		if not O00OOO00OOOOO0O00 ['status']:#line:44
			frappe .throw (O00OOO00OOOOO0O00 ['message'])#line:45
		return O00OOO00OOOOO0O00 #line:46
	return frappe .throw (f"status_code: {OO000OOO00O0OO00O.status_code}, there is an issue in the server")#line:48
@frappe .whitelist ()#line:52
def check_compute_payee (O0O0OOOOO00OOOOO0 ):#line:53
	if type (O0O0OOOOO00OOOOO0 )==str :#line:54
		O0O0OOOOO00OOOOO0 =frappe ._dict (json .loads (O0O0OOOOO00OOOOO0 ))#line:55
	OOOOOO00O0O0OOO0O =frappe .get_doc ("Employee",O0O0OOOOO00OOOOO0 .employee ).as_dict ()#line:56
	O0OOO0O00OO000O0O =getdate (O0O0OOOOO00OOOOO0 .start_date )#line:58
	OOOOOOOOOOOOO0OO0 =(OOOOOO00O0O0OOO0O .date_of_joining if OOOOOO00O0O0OOO0O .date_of_joining >O0OOO0O00OO000O0O else O0OOO0O00OO000O0O )#line:61
	O0000O00OO0000OOO =frappe .get_value ("Salary Structure Assignment",{"employee":O0O0OOOOO00OOOOO0 .employee ,"salary_structure":O0O0OOOOO00OOOOO0 .salary_structure ,"from_date":("<=",OOOOOOOOOOOOO0OO0 ),"docstatus":1 ,},"*",order_by ="from_date desc",as_dict =True ,)#line:73
	if O0000O00OO0000OOO .compute_payee :#line:74
		O0000000OOO00O000 =frappe .get_doc ('NGN PAYE Config')#line:75
		return frappe ._dict (calculate_values (O0O0OOOOO00OOOOO0 ,O0000000OOO00O000 ))#line:76
	return frappe ._dict ({'status':False })#line:77
