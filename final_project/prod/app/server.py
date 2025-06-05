from flask import Flask, request, jsonify
import pickle
import numpy as np

with open('models/pipeline.pkl','rb') as f:
    pipeline = pickle.load(f)
with open('models/logreg.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() 
    features = data['features']
    features = np.array(features).reshape(1,-1)
    features = pipeline.transform(features)
    prediction = model.predict(features)
    
    return jsonify({
        'prediction': int(prediction[0])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)