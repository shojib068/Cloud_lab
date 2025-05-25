from flask import Flask, render_template, request

app = Flask(__name__)

# Root URL renders the form
@app.route('/', methods=['GET'])
def index():
    return render_template('nth_largest.html')

@app.route('/nth_largest', methods=['GET', 'POST'])
def nth_largest():
    if request.method == 'POST':
        numbers = list(map(int, request.form['numbers'].split(',')))
        n = int(request.form['n'])
        sorted_numbers = sorted(numbers, reverse=True)
        nth_largest = sorted_numbers[n - 1] if n <= len(numbers) else None

        return render_template('nth_largest.html', nth_largest=nth_largest)
    return render_template('nth_largest.html')

if __name__ == '__main__':
    app.run(debug=True)
