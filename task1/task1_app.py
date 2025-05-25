from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        n = int(request.form['n'])
        even_numbers = [2 * i for i in range(1, n + 1)]
        return render_template('index.html', numbers=even_numbers)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
