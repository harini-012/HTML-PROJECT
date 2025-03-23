from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/"  ,methods=["GET","POST"])
def form():
    if request.method =='POST':
        data={"name":request.form.get('name'),
        "age":request.form.get('no'),
        "gender":request.form.get('gender'),
        "email":request.form.get('email'),
        "group":request.form.get('group'),
        "month":request.form.get('mon'),
        "time":request.form.get('time'),
        "file":request.files.get('file').filename if request.files.get('file') else "No file uploaded",
        }
        return render_template("project2result.html",data=data)
    return render_template("project2booking.html") 
        
@app.route("/certificate")
def certificate():
    return render_template("project2certificate.html")
if __name__=='__main__':
    app.run(debug=True)
        
        