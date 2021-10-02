from flask import Flask
app=Flask(__name__)

@app.route("/")
def mainapp():
    return "Hi there it is Flask main page with fix 101...changes done for some fix"


@app.route("/<page_name>")
def endpage(page_name):
    return "Bye there you have reached {}".format(page_name)

if __name__== "__main__":
    app.run(debug=True,host="0.0.0.0")
