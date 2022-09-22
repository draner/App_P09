from flask import Flask, render_template, request, flash
import requests as req
import pandas as pd

url = " https://reco-p09.azurewebsites.net/api/article_rec?user_id="

# Functions
def prediction(user_id):

    response = req.get(url+str(user_id))
    response = response.json()
    response = pd.DataFrame(response)
    response = response.to_html()
    response = (f"<p>Recommendations for user {user_id}</p>") + response
    return response

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'some_secret'
@app.route('/predict')

def index():
    return render_template('index.html')

@app.route('/predicted', methods=['POST', 'GET'])
def predicted():
    if request.method == 'POST':
        client_id = request.form['client_id']
        predictions = prediction(client_id)
        flash(predictions, 'prediction')
        return render_template('index.html')