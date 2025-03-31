from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/" ,methods=["GET","POST"])
def form():
    if request.method =="POST":
        data={"question1":request.form.get("question1"),
        "question2":request.form.get("question2"),
        "question3":request.form.get("question3"),
        "question4":request.form.get("question4"),
        "question5":request.form.get("question5"),}
        return render_template("project3result.html",data=data)
    return render_template("project3quiz.html")
@app.route("/marks",methods=["GET"])

def marks():
    
    q1=1 if request.args.get("question1")=="Event Horizon" else 0
      
    q2=1 if request.args.get("question2")=="A massive star" else 0
      
    q3=1 if request.args.get("question3")=="Singularity" else 0
       
    q4=1 if request.args.get("question4")=="M87" else 0
        
    q5=1 if request.args.get("question5")=="gravity" else 0
 
    tot_marks=q1+q2+q3+q4+q5
  
    return render_template("project3marks.html",tot_marks=tot_marks)

     
    
if __name__=='__main__':
    app.run(debug=True)
    