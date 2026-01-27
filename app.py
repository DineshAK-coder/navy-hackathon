import os
from flask import Flask, jsonify, render_template

# This tells Flask exactly where to look for your HTML files on the Vercel server
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    # Make sure your file is named index.html inside the templates folder
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Path fix for the CSV file as well
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'processed_results.csv')
    
    try:
        import pandas as pd
        df = pd.read_csv(file_path)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Required for Vercel
if __name__ == '__main__':
    app.run()