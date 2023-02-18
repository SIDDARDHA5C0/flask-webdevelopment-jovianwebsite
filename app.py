from flask import Flask
#importing the Flask
app=Flask(__name__)
#creating a flask object
#decorator,registered an route
@app.route("/")
def helloworld():
  return "hello ask the wrold"

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
