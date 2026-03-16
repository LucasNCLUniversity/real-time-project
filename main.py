#imports
from flask import Flask, render_template #for the frontend

#flask logic for setting up index
app = Flask('testapp')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()