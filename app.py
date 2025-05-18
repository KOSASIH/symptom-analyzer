from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
from medical_knowledge import MEDICAL_KNOWLEDGE
from symptom_relations import get_related_symptoms
from severity_assessment import assess_severity

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_symptoms():
    data = request.json
    symptoms = data.get('symptoms', '').lower()
    
    # Simple symptom analysis based on keyword matching
    symptom_list = [s.strip() for s in symptoms.split(',')]
    
    # Get related symptoms
    related_symptoms = get_related_symptoms(symptom_list)
    
    # Assess severity
    severity = assess_severity(symptom_list)
    
    results = {}
    for symptom in symptom_list:
        if symptom in MEDICAL_KNOWLEDGE:
            results[symptom] = MEDICAL_KNOWLEDGE[symptom]
        else:
            # If symptom not found in our knowledge base
            results[symptom] = {
                "conditions": ["Unknown - please consult a healthcare professional"],
                "recommendations": ["Consult a healthcare professional for proper diagnosis"]
            }
    
    return jsonify({
        "analysis": results,
        "related_symptoms": related_symptoms,
        "severity_assessment": severity,
        "disclaimer": "This is not medical advice. Always consult with a healthcare professional for proper diagnosis and treatment."
    })

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    app.run(host='0.0.0.0', port=8080, debug=True)