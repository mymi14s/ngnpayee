const _0x5c0db1=_0x424a;function _0x424a(_0x4fa8dd,_0xef5424){const _0x366b45=_0x366b();return _0x424a=function(_0x424adf,_0x220445){_0x424adf=_0x424adf-0x1ee;let _0x40b47b=_0x366b45[_0x424adf];return _0x40b47b;},_0x424a(_0x4fa8dd,_0xef5424);}(function(_0x296f3b,_0x37bd3e){const _0x11697e=_0x424a,_0x4080b3=_0x296f3b();while(!![]){try{const _0x3048b4=-parseInt(_0x11697e(0x205))/0x1+parseInt(_0x11697e(0x1fc))/0x2*(parseInt(_0x11697e(0x1f8))/0x3)+-parseInt(_0x11697e(0x204))/0x4*(-parseInt(_0x11697e(0x1f0))/0x5)+parseInt(_0x11697e(0x1ee))/0x6*(parseInt(_0x11697e(0x209))/0x7)+-parseInt(_0x11697e(0x203))/0x8*(-parseInt(_0x11697e(0x208))/0x9)+-parseInt(_0x11697e(0x1f1))/0xa+-parseInt(_0x11697e(0x1ff))/0xb*(parseInt(_0x11697e(0x200))/0xc);if(_0x3048b4===_0x37bd3e)break;else _0x4080b3['push'](_0x4080b3['shift']());}catch(_0x22946a){_0x4080b3['push'](_0x4080b3['shift']());}}}(_0x366b,0xc922f),frappe['ui'][_0x5c0db1(0x1f3)]['on']('Salary\x20Slip',{'refresh'(_0x4a8ce8){const _0x312593=_0x5c0db1;if(_0x4a8ce8[_0x312593(0x1fd)][_0x312593(0x20a)]==_0x312593(0x1f5)){}},'setup'(_0x2ab5a9){const _0xabc6b4=_0x5c0db1;_0x2ab5a9[_0xabc6b4(0x1f2)]={};},'employee':function(_0x409b8c){const _0x47070e=_0x5c0db1;frappe[_0x47070e(0x1ef)]({'method':_0x47070e(0x206),'type':'POST','args':{'OO000O00OOO00OOOO':_0x409b8c[_0x47070e(0x1fd)]},'callback':function(_0x244dd9){const _0x387068=_0x47070e;if(_0x244dd9['message'][_0x387068(0x20a)]){let _0x39df34=_0x244dd9[_0x387068(0x202)]['total'];_0x409b8c[_0x387068(0x1fd)][_0x387068(0x20b)][_0x387068(0x201)]?(_0x409b8c[_0x387068(0x1fd)]['deductions'][_0x387068(0x1fe)](_0x1e2795=>{const _0xbb6919=_0x387068;_0x1e2795[_0xbb6919(0x20c)]==_0xbb6919(0x1fa)?_0x1e2795[_0xbb6919(0x207)]=_0x39df34:_0x409b8c['add_child']('deductions',{'salary_component':_0xbb6919(0x1fa),'amount':_0x39df34});}),_0x409b8c[_0x387068(0x1f4)](_0x387068(0x20b)),set_totals(_0x409b8c)):(_0x409b8c[_0x387068(0x1fb)](_0x387068(0x20b),{'salary_component':_0x387068(0x1fa),'amount':_0x39df34}),_0x409b8c[_0x387068(0x1f4)](_0x387068(0x20b)),set_totals(_0x409b8c));}}});}}));var set_totals=function(_0x26ffca){const _0x5c3de2=_0x5c0db1;_0x26ffca[_0x5c3de2(0x1fd)][_0x5c3de2(0x1f9)]===0x0&&_0x26ffca['doc'][_0x5c3de2(0x1f6)]===_0x5c3de2(0x20d)&&((_0x26ffca[_0x5c3de2(0x1fd)][_0x5c3de2(0x1f7)]||_0x26ffca['doc'][_0x5c3de2(0x20b)])&&frappe[_0x5c3de2(0x1ef)]({'method':'set_totals','doc':_0x26ffca[_0x5c3de2(0x1fd)],'callback':function(){_0x26ffca['refresh_fields']();}}));};function _0x366b(){const _0x33c7f6=['6lYfwrR','call','4720zPIpik','558630KdWpWg','fns','form','refresh_field','Draft','doctype','earnings','195006lXxLnS','docstatus','PAYE','add_child','8kzmGti','doc','forEach','308OSJAHz','475572ZPORqo','length','message','875704MDALFT','4564jFOOQs','134223bTJKxO','ngnpayee.events.salary_slip.check_compute_payee','amount','54CKSMzW','908033bkpkMX','status','deductions','salary_component','Salary\x20Slip'];_0x366b=function(){return _0x33c7f6;};return _0x366b();}