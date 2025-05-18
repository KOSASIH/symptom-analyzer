"""
Severity assessment for the SymptomAnalyzer application.
This contains logic to assess the severity of symptoms and provide urgency recommendations.
"""

# Symptoms that might indicate a medical emergency
EMERGENCY_SYMPTOMS = [
    "chest pain",
    "severe shortness of breath",
    "sudden severe headache",
    "sudden numbness",
    "sudden weakness",
    "sudden difficulty speaking",
    "sudden vision changes",
    "severe abdominal pain",
    "coughing up blood",
    "vomiting blood",
    "severe bleeding",
    "suicidal thoughts",
    "seizure",
    "loss of consciousness",
    "severe allergic reaction"
]

# Symptoms that warrant urgent care (within 24 hours)
URGENT_SYMPTOMS = [
    "high fever",
    "persistent vomiting",
    "severe dehydration",
    "moderate shortness of breath",
    "persistent chest discomfort",
    "moderate abdominal pain",
    "severe joint pain",
    "severe back pain",
    "severe headache",
    "eye pain",
    "ear pain with fever",
    "rash with fever",
    "persistent dizziness",
    "severe sore throat with difficulty swallowing",
    "severe cough"
]

# Combinations of symptoms that increase severity
CONCERNING_COMBINATIONS = [
    {"fever", "rash"},
    {"headache", "fever", "stiff neck"},
    {"fever", "cough", "shortness of breath"},
    {"abdominal pain", "fever", "vomiting"},
    {"chest pain", "shortness of breath"},
    {"headache", "vision changes"},
    {"dizziness", "chest pain"},
    {"fever", "persistent cough", "fatigue"}
]

def assess_severity(symptom_list):
    """
    Assess the severity of symptoms and provide an urgency recommendation.
    
    Returns a dictionary with:
    - severity_level: "emergency", "urgent", "moderate", or "mild"
    - recommendation: Text explaining what to do
    - reasoning: Explanation of why this severity level was assigned
    """
    # Convert to lowercase for matching
    symptoms_lower = [s.lower() for s in symptom_list]
    
    # Check for emergency symptoms
    for symptom in EMERGENCY_SYMPTOMS:
        if any(symptom in s for s in symptoms_lower):
            return {
                "severity_level": "emergency",
                "recommendation": "Seek immediate medical attention. Call emergency services or go to the nearest emergency room.",
                "reasoning": f"You reported '{symptom}', which may indicate a serious medical condition requiring immediate attention."
            }
    
    # Check for urgent symptoms
    for symptom in URGENT_SYMPTOMS:
        if any(symptom in s for s in symptoms_lower):
            return {
                "severity_level": "urgent",
                "recommendation": "Contact a healthcare provider today or visit an urgent care facility.",
                "reasoning": f"You reported '{symptom}', which may require prompt medical attention within 24 hours."
            }
    
    # Check for concerning combinations
    symptoms_set = set(symptoms_lower)
    for combo in CONCERNING_COMBINATIONS:
        if combo.issubset(symptoms_set):
            return {
                "severity_level": "urgent",
                "recommendation": "Contact a healthcare provider today or visit an urgent care facility.",
                "reasoning": f"The combination of symptoms you reported ({', '.join(combo)}) may indicate a condition requiring prompt medical attention."
            }
    
    # If multiple symptoms (3+), consider it moderate
    if len(symptom_list) >= 3:
        return {
            "severity_level": "moderate",
            "recommendation": "Consider scheduling an appointment with a healthcare provider in the next few days.",
            "reasoning": "You're experiencing multiple symptoms which, while not immediately concerning, should be evaluated by a healthcare professional."
        }
    
    # Default to mild
    return {
        "severity_level": "mild",
        "recommendation": "Monitor your symptoms. If they persist or worsen, consider contacting a healthcare provider.",
        "reasoning": "Based on the information provided, your symptoms appear to be mild. However, this is not a substitute for professional medical advice."
    }