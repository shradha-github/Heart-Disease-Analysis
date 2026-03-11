from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    age = int(request.form["age"])
    bp = int(request.form["bp"])
    cholesterol = int(request.form["cholesterol"])
    heart_rate = int(request.form["heart_rate"])

    risk_score = 0

    if age > 50:
        risk_score += 1

    if bp > 140:
        risk_score += 1

    if cholesterol > 240:
        risk_score += 1

    if heart_rate > 100:
        risk_score += 1

    if risk_score >= 3:
        result = "⚠ High Risk of Heart Disease"
    elif risk_score == 2:
        result = "⚠ Moderate Risk"
    else:
        result = "✅ Low Risk"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
