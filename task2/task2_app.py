from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('multiply_matrices'))

@app.route('/multiply_matrices', methods=['GET', 'POST'])
def multiply_matrices():
    if request.method == 'POST':
        matrix1 = [[int(x) for x in request.form['matrix1'].split(',')]]
        matrix2 = [[int(x) for x in request.form['matrix2'].split(',')]]

        # Matrix multiplication logic
        result = [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]

        return render_template('matrix.html', result=result)
    return render_template('matrix.html')

if __name__ == '__main__':
    app.run(debug=True)
