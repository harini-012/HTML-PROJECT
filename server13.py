from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)
orders=[]

@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={"name":request.form.get("name"),
        "contact":request.form.get("cno"),
        "address":request.form.get("add"),
        "pin":request.form.get("pin"),
        "payment":request.form.get("mode"),
        "premium":request.form.get("premi"),
        "category":request.form.get("category"),
        "pname":request.form.get("pname"),
        "coupon":request.files.get("coupon").filename if request.files.get("coupon") else "No photo updated",
        }
        orders.append(data)
        return render_template("project5result.html",all_orders=orders)
    return render_template("project5form.html")
    
    
if __name__=='__main__':
    app.run(debug=True)
        