frappe.ui.form.on('Salary Slip', {
	refresh(frm) {
		// your code here
    if(frm.doc.status == "Draft"){
      // frm.disable_save()
    }
	},
	setup(frm){
	    frm.fns = {}
	},
// 	emloyee
  employee: function(frm){
        // update PAYE
        frappe.call({
            method: "ngnpayee.events.salary_slip.check_compute_payee", //dotted path to server method
            type: 'POST',
            args: {doc:frm.doc},
            callback: function(r) {

              if(r.message.status){
                let total = r.message.total;
                if(frm.doc.deductions.length){
                    frm.doc.deductions.forEach(d=>{
                      if(d.salary_component=="PAYE"){
                          d.amount = total
                        } else {

                        frm.add_child('deductions', {
                              salary_component: 'PAYE',
                              amount: total,
                          });
                        }
                    })
                    frm.refresh_field('deductions');
                    set_totals(frm);
                } else {
                    frm.add_child('deductions', {
                        salary_component: 'PAYE',
                        amount: total,
                    });
                    frm.refresh_field('deductions');
                    set_totals(frm);
                }
              }
            }
        });

  }
})


var set_totals = function(frm) {
	if (frm.doc.docstatus === 0 && frm.doc.doctype === "Salary Slip") {
		if (frm.doc.earnings || frm.doc.deductions) {
			frappe.call({
				method: "set_totals",
				doc: frm.doc,
				callback: function() {
					frm.refresh_fields();
				}
			});
		}
	}
};
