from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newUser', methods=['POST'])
def from_submit():
    print("*"*100)
    print("HERE IS WHAT WE GOT")
    user_name = request.form['UserName']
    password = request.form['Password']
    print(request.form)
    #return render_template('result.html', user_name = user_name, password = password)
    return redirect(f"/success/{user_name}/{password}")

@app.route('/success/<name>/<password>')
def success(name, password):
    return render_template('result.html', user_name = name, password = password)


if __name__=='__main__':
    app.run(debug=True)