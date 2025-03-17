from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def form():
    if request.method =='POST':
        data={"name":request.form.get('name'),
        "email":request.form.get('email'),
        "gender":request.form.get('gender'),
        "cno":request.form.get('phone'),
        "eventtype":request.form.get('type'),
        "date":request.form.get('date'),
        "guests":request.form.get('guests'),
        "additional":request.form.get('additional'),
        "venue":request.form.get('venue'),
        "file":request.files.get('file').filename if request.files.get('file') else "No file uploaded",
        "pay":request.form.get('pay')
        }
        return render_template("projectresult.html",data=data)
    return render_template("projectform.html")
if __name__=='__main__':
    app.run(debug=True)
        
        