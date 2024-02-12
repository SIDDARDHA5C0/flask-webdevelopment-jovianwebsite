from flask import Flask, render_template,jsonify
#importing the Flask
app = Flask(__name__)
#creating a flask object

JOBS = [
  {
    "id": 1,
    "role": "data analyst",
    "location": "india",
    "salary": 100000
  },
  {
    "id": 2,
    "role": "data scientist",
    "location": "india",
    "salary": 300000
  },
  {
    "id": 3,
    "role": "data engineer",
    "location": "india",
    "salary": 400000
  },
  {
    "id": 4,
    "role": "machine engineer",
    "location": "india",
    "salary": 500000
  },
]


#decorator,registered an route
@app.route("/")
def helloworld():
  return render_template("home.html", jobs=JOBS,company_name="Jovian")

@app.route("/api/jobs")
def jjobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

