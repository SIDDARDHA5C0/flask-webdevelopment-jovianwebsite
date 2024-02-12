from flask import Flask, render_template
#importing the Flask
app = Flask(__name__)
#creating a flask object

JOBS = [
  {
    "id": 1,
    "role": "data analyst",
    "location": "india",
    "salary": "100000"
  },
  {
    "id": 2,
    "role": "data scientist",
    "location": "india",
    "salary": "100000"
  },
  {
    "id": 3,
    "role": "data engineer",
    "location": "india",
    "salary": "100000"
  },
  {
    "id": 4,
    "role": "machine engineer",
    "location": "india",
    "salary": "100000"
  },
]


#decorator,registered an route
@app.route("/")
def helloworld():
  return render_template("home.html", jobs=JOBS,company_name="Jovian")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

