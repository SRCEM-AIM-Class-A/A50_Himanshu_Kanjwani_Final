from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home.html template
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        # Render greet.html with name and age variables
        return render_template('greet.html', name=name, age=age)
    
    # Render the greet.html template for GET request
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)
