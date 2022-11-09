from app import *




@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')



@app.route("/signin", methods=["POST", "GET"])
def index():
    if request.method=="GET":
        return render_template('signin.html')


@app.route("/signup", methods=["POST", "GET"])
def index():
    if request.method=="GET":
        return render_template('signup.html')


@app.route("/upload", methods=["POST", "GET"])
def index():
    if request.method=="GET":      
        return render_template('upload.html')




if __name__ == "__main__":
  app.run(debug=True)