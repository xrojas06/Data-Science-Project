from flask import Flask, request, jsonify
import mlflow.keras
import numpy as np

app = Flask(__name__)
model = None

with open("run_id.txt", "r") as f:
    run_id = f.read().strip()

def load_mlflow_model():
    global model
    model = mlflow.keras.load_model(f"runs:/{run_id}/lstm_model")

if __name__ == '__main__':
    load_mlflow_model()
    app.run(debug=True)
