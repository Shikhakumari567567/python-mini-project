
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]

        subjects = ["English", "Math", "Science", "Computer", "Hindi"]

        marks = [
            float(request.form[subject])
            for subject in subjects
        ]

        if any(mark < 0 or mark > 100 for mark in marks):
            return render_template(
                "index.html",
                error="Marks must be between 0 and 100."
            )

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        status = "Pass" if all(mark >= 33 for mark in marks) else "Fail"

        result = {
            "name": name,
            "total": total,
            "percentage": round(percentage, 2),
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
