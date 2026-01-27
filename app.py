from flask import Flask, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# This is the "Entry Point" Vercel looks for
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Use relative pathing to ensure it finds the CSV in the Vercel environment
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'processed_results.csv')
    df = pd.read_csv(file_path)
    return jsonify(df.to_dict(orient='records'))

# Vercel doesn't use app.run(), but keeping this for local testing is fine
if __name__ == '__main__':
    app.run(debug=True)