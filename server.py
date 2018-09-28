from flask import Flask, session, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)

