from flask import Flask, render_template, request

app = Flask(__name__)
database = ['charishma','anusha','bhavani','apurva','manasa']


#######################
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/thankyou", methods=['POST'])
def registration():
    uname = request.form.get("user_name")
    uage = int(request.form.get("user_age"))
    return render_template("thankyou.html", uname=uname, uage=uage)

# Dynamic Routing
@app.route('/in/<user_name>')
def user_profile(user_name):
    if user_name in database:
        return render_template("user_profile.html", uname=user_name)
    return "kindly register and comeback"
#############################

# 127.0.0.1 => Loop Back Address
# 0.0.0.0 => Broadcasting Address

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")