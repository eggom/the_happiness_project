from flask import Flask, request, render_template
from sqlalchemy import create_engine
import pickle
import numpy as np
import sql.load_to_sql as load_to_sql
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

# Load the model and scaler at startup
model = pickle.load(open('../models/random_forest_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))

# Load your dataset
engine = create_engine('sqlite:///happiness_data.sqlite', echo=False)

@app.route('/', methods=['GET'])
def home():
    # Render the home page with form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture data from the form
     try:
        GDPperCapita = float(int(request.form['gdp'])/4)
        Family = float(int(request.form['social'])/5)
        LifeExpectancy = float(int(request.form['health'])/7)
        Freedom = float(int(request.form['freedom'])/10)
        NoCorruption = float(int(request.form['corruption'])/10)
        Generosity = float(int(request.form['generosity'])/10)
        DystopiaResidual = float(int(request.form['dystopia'])/2.5)
        
        # Create a feature array for prediction
        features = np.array([[GDPperCapita, Family, LifeExpectancy, Freedom,
                              NoCorruption, Generosity, DystopiaResidual]])
                              
        # Scale the feature array
        features_scaled = scaler.transform(features)
        
        # Make a prediction
        prediction = model.predict(features_scaled)
        
        # Interpret the prediction
        prediction_text = 'Happy' if prediction[0] == 1 else 'Not Happy'
        
     except ValueError as e:
        # Handle the error if the input is not a valid float
        prediction = f"Invalid input detected. Please enter valid numbers. Error: {e}"
        
     other_scores = {}
     with engine.connect() as connection:
        for variable in ['GDPperCapita', 'Family', 'LifeExpectancy', 'Freedom', 'NoCorruption', 'Generosity',
                         'DystopiaResidual']:
            scores = connection.execute(f"SELECT {variable} FROM happiness_data").fetchall()
            other_scores[variable] = [score[0] for score in scores]
    
     your_scores = [GDPperCapita, Family, LifeExpectancy, Freedom, NoCorruption, Generosity, DystopiaResidual]

     graph = create_graph(your_scores, other_scores)

    # Render the page with the prediction results
     return render_template('result.html', prediction_text=f'Prediction: You are {prediction_text}', graph=graph)

def create_graph(your_scores, other_scores):
    data = []
    line_colors = ['#264653', '#287271', '#2A9D8F', '#E9C46A', '#efb366', '#F4A261', '#EE8959', '#E76F51']
    # Add traces for each variable
    for i, (variable, scores) in enumerate(other_scores.items()):
        trace = go.Box(x=scores, name=variable, fillcolor='#f9f7f3', line=dict(color=(line_colors[i % len(line_colors)])))
        data.append(trace)
    
    user_trace = go.Scatter(
            x=your_scores,
            y=['GDPperCapita','Family','LifeExpectancy','Freedom','NoCorruption','Generosity', 'DystopiaResidual'],
            mode='markers',
            marker=dict(color='#dc143c'),
            name='Your Score'
        )
    data.append(user_trace)
    
    layout = go.Layout(title='Comparison of Your Score with the Rest of the World', xaxis=dict(title='Happiness Score'), yaxis=dict(title='Variables'))
    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False)
    return graph

if __name__ == '__main__':
    load_to_sql.load_data_to_sql()
    app.run(debug=True)
