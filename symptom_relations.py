"""
Symptom relations for the SymptomAnalyzer application.
This contains mappings of symptoms to related symptoms that often occur together.
"""

SYMPTOM_RELATIONS = {
    "headache": ["fever", "nausea", "dizziness", "fatigue", "sore throat"],
    "fever": ["headache", "cough", "sore throat", "fatigue", "body aches"],
    "cough": ["fever", "sore throat", "shortness of breath", "chest pain", "fatigue"],
    "fatigue": ["headache", "fever", "insomnia", "anxiety", "joint pain"],
    "nausea": ["headache", "abdominal pain", "dizziness", "fever", "fatigue"],
    "dizziness": ["headache", "nausea", "fatigue", "shortness of breath", "anxiety"],
    "chest pain": ["shortness of breath", "cough", "fatigue", "dizziness", "anxiety"],
    "shortness of breath": ["chest pain", "cough", "fatigue", "anxiety", "fever"],
    "abdominal pain": ["nausea", "fever", "diarrhea", "fatigue", "back pain"],
    "joint pain": ["fatigue", "fever", "rash", "back pain", "headache"],
    "rash": ["fever", "joint pain", "fatigue", "sore throat", "headache"],
    "sore throat": ["cough", "fever", "headache", "fatigue", "shortness of breath"],
    "back pain": ["abdominal pain", "joint pain", "fatigue", "fever", "headache"],
    "insomnia": ["fatigue", "anxiety", "headache", "depression", "chest pain"],
    "anxiety": ["insomnia", "fatigue", "chest pain", "shortness of breath", "headache"]
}

def get_related_symptoms(symptom_list):
    """
    Get related symptoms based on the provided list of symptoms.
    Returns a list of related symptoms not already in the input list.
    """
    related = set()
    for symptom in symptom_list:
        if symptom in SYMPTOM_RELATIONS:
            related.update(SYMPTOM_RELATIONS[symptom])
    
    # Remove symptoms that are already in the input list
    related = related - set(symptom_list)
    
    # Return as a list, limited to top 5 related symptoms
    return list(related)[:5]