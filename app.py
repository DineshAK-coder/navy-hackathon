from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # This will serve your main HTML file
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Load the processed ML results
    df = pd.read_csv('processed_results.csv')
    # Convert to JSON for the frontend
    return jsonify(df.to_dict(orient='records'))

# Change app.run() to this so Vercel can find the 'app' object
app = Flask(__name__)

# ... your routes ...

# Vercel needs the 'app' variable, it doesn't use the __main__ block
if __name__ == '__main__':
    app.run()