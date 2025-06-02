from flask import Flask, request, render_template
app =Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return render_template("project4front.html")


@app.route("/quiz", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = {"question1": request.form.get("question1"),
       "question2": request.form.get("question2"),
       "question3": request.form.get("question3"),
       "question4": request.form.get("question4"),
       "question5": request.form.get("question5"),
        }
        return render_template("project4quizresult.html", data=data)
    return render_template("project4quiz.html")

@app.route("/shows", methods=["GET"])
def shows():
    return render_template("project4shows.html")



@app.route("/amenities", methods=["GET"])
def aboutus():
    return render_template("project4amenities.html")

@app.route("/visitus", methods=["GET"])
def visitus():
    return render_template("project4visitus.html")

@app.route("/food", methods=["GET"])
def food():
    return render_template("project4food.html")

@app.route("/desserts", methods=["GET"])
def desserts():
    return render_template("project4desserts.html")

@app.route("/beverages", methods=["GET"])
def beverages():
    return render_template("project4beverages.html")

@app.route("/combos", methods=["GET"])
def combos():
    return render_template("project4combos.html")

@app.route("/bookticket", methods=["GET", "POST"])
def bookticket():
    return render_template("project4bookticket.html")


@app.route("/marks", methods=["GET"])
def marks():
    q1 = 1 if request.args.get("question1") == "Amaran" else 0
    q2 = 1 if request.args.get("question2") == "Sachien" else 0
    q3 = 1 if request.args.get("question3") == "AK" else 0
    q4 = 1 if request.args.get("question4") == "SooraraiPottrui" else 0
    q5 = 1 if request.args.get("question5") == "ARR" else 0

    tot_marks = q1 + q2 + q3 + q4 + q5

    if tot_marks >= 3:
        result = "You are eligible for an offer"
        return render_template("project4marks.html", tot_marks=tot_marks, result=result)
    else:
        result = "You are not eligible for an offer, try again"
        return render_template("project4marks.html", tot_marks=tot_marks, result=result)


@app.route("/bookresult", methods=["GET", "POST"])
def bookresult():
    booked = ["A1", "A4", "D3", "D", "X", "W5", "Z1", "E", "G2", "H"]
    if request.method == "POST":
        theatre = {
       "date": request.form.get("date"),
       "movie": request.form.get("movie"),
       "seat": request.form.getlist("seat"),
       "mall": request.form.get("mall"),
       "time": request.form.get("time"),
        }
        booked_seats = []
        available_seats = []
        for seat in theatre["seat"]:
            if seat in booked:
                booked_seats.append(seat)
            else:
                available_seats.append(seat)

        if booked_seats:
          
            info = ",".join(booked_seats) + "Already booked.Go back to booking page"
            return render_template("project4confirmation.html", info=info,theatre=theatre)
        else:
            
            booked.extend(available_seats) 
            return render_template("project4confirmation.html", theatre=theatre)

    return render_template("project4bookticket.html")

if __name__ == '__main__':
    app.run(debug=True)