"""
Medical knowledge base for the SymptomAnalyzer application.
This contains mappings of symptoms to potential conditions and recommendations.
"""

MEDICAL_KNOWLEDGE = {
    "headache": {
        "conditions": [
            "Migraine", 
            "Tension headache", 
            "Sinusitis", 
            "Dehydration", 
            "High blood pressure", 
            "Concussion",
            "Medication side effect"
        ],
        "recommendations": [
            "Rest in a quiet, dark room", 
            "Stay hydrated", 
            "Consider over-the-counter pain relievers", 
            "Apply cold or warm compress to the forehead or neck",
            "Practice relaxation techniques",
            "Consult a doctor if severe, sudden, or accompanied by other symptoms"
        ]
    },
    "fever": {
        "conditions": [
            "Viral infection", 
            "Bacterial infection", 
            "Inflammation", 
            "Heat exhaustion",
            "Medication reaction",
            "Autoimmune disorder"
        ],
        "recommendations": [
            "Stay hydrated", 
            "Rest", 
            "Take fever-reducing medication if needed", 
            "Use a cool compress",
            "Wear lightweight clothing",
            "Seek medical attention if fever is high (above 103°F/39.4°C) or persistent"
        ]
    },
    "cough": {
        "conditions": [
            "Common cold", 
            "Flu", 
            "Bronchitis", 
            "Allergies", 
            "COVID-19",
            "Asthma",
            "GERD (acid reflux)",
            "Pneumonia"
        ],
        "recommendations": [
            "Stay hydrated", 
            "Rest", 
            "Use cough suppressants for dry cough or expectorants for productive cough", 
            "Use a humidifier",
            "Avoid irritants like smoke",
            "Seek medical attention if cough is severe, produces blood, or lasts more than 2 weeks"
        ]
    },
    "fatigue": {
        "conditions": [
            "Lack of sleep", 
            "Stress", 
            "Anemia", 
            "Depression", 
            "Hypothyroidism",
            "Chronic fatigue syndrome",
            "Sleep apnea",
            "Diabetes",
            "Heart disease"
        ],
        "recommendations": [
            "Ensure adequate sleep (7-9 hours)", 
            "Manage stress through relaxation techniques", 
            "Eat a balanced diet", 
            "Stay physically active",
            "Limit caffeine and alcohol",
            "Consider medical evaluation if persistent"
        ]
    },
    "nausea": {
        "conditions": [
            "Food poisoning", 
            "Gastroenteritis", 
            "Migraine", 
            "Pregnancy", 
            "Medication side effect",
            "Motion sickness",
            "Anxiety",
            "Vestibular disorders"
        ],
        "recommendations": [
            "Stay hydrated with small sips of clear fluids", 
            "Eat bland foods like crackers or toast", 
            "Avoid strong odors and triggering foods", 
            "Try ginger tea or candies",
            "Rest in a cool, quiet environment",
            "Seek medical attention if severe, persistent, or accompanied by severe abdominal pain"
        ]
    },
    "dizziness": {
        "conditions": [
            "Inner ear problems", 
            "Low blood pressure", 
            "Dehydration", 
            "Anemia", 
            "Medication side effect",
            "Anxiety",
            "Hypoglycemia (low blood sugar)",
            "Neurological conditions"
        ],
        "recommendations": [
            "Sit or lie down immediately", 
            "Stay hydrated", 
            "Move slowly when changing positions", 
            "Avoid sudden movements",
            "Ensure adequate food intake",
            "Seek medical attention if severe, recurrent, or accompanied by other symptoms"
        ]
    },
    "chest pain": {
        "conditions": [
            "Angina", 
            "Heart attack", 
            "Pulmonary embolism", 
            "Pneumonia", 
            "Acid reflux",
            "Muscle strain",
            "Anxiety/panic attack",
            "Costochondritis (inflammation of rib cartilage)"
        ],
        "recommendations": [
            "Seek immediate medical attention, especially if pain is severe, crushing, or accompanied by shortness of breath, sweating, or nausea", 
            "Rest in a comfortable position", 
            "Take prescribed medications if applicable", 
            "Do not drive yourself to the hospital if you suspect a heart attack"
        ]
    },
    "shortness of breath": {
        "conditions": [
            "Asthma", 
            "COPD", 
            "Heart failure", 
            "Pneumonia", 
            "Anxiety",
            "Pulmonary embolism",
            "Anemia",
            "COVID-19"
        ],
        "recommendations": [
            "Sit upright to ease breathing", 
            "Use prescribed inhalers if applicable", 
            "Practice slow, deep breathing", 
            "Avoid triggers like smoke or allergens",
            "Seek immediate medical attention if severe or accompanied by chest pain, blue lips, or confusion"
        ]
    },
    "abdominal pain": {
        "conditions": [
            "Gastritis", 
            "Appendicitis", 
            "Gallstones", 
            "Kidney stones", 
            "Irritable bowel syndrome",
            "Inflammatory bowel disease",
            "Pancreatitis",
            "Diverticulitis",
            "Food poisoning"
        ],
        "recommendations": [
            "Rest and avoid solid foods temporarily", 
            "Stay hydrated", 
            "Use a heating pad for comfort", 
            "Take over-the-counter pain relievers if appropriate",
            "Seek immediate medical attention if pain is severe, persistent, or accompanied by fever, vomiting, or blood in stool"
        ]
    },
    "joint pain": {
        "conditions": [
            "Arthritis", 
            "Gout", 
            "Bursitis", 
            "Tendinitis", 
            "Lupus",
            "Lyme disease",
            "Fibromyalgia",
            "Injury or strain"
        ],
        "recommendations": [
            "Rest the affected joint", 
            "Apply ice for acute pain or heat for chronic pain", 
            "Take over-the-counter anti-inflammatory medications if appropriate", 
            "Maintain a healthy weight",
            "Consider gentle exercises like swimming or walking",
            "Seek medical attention if pain is severe, accompanied by significant swelling, or limits mobility"
        ]
    },
    "rash": {
        "conditions": [
            "Allergic reaction", 
            "Eczema", 
            "Psoriasis", 
            "Contact dermatitis", 
            "Fungal infection",
            "Viral infection (like chickenpox or measles)",
            "Hives",
            "Heat rash"
        ],
        "recommendations": [
            "Avoid scratching", 
            "Keep the area clean and dry", 
            "Use mild, fragrance-free soaps", 
            "Apply over-the-counter hydrocortisone cream for itching",
            "Take an antihistamine if allergic reaction is suspected",
            "Seek medical attention if rash is widespread, painful, blistering, or accompanied by fever"
        ]
    },
    "sore throat": {
        "conditions": [
            "Common cold", 
            "Strep throat", 
            "Tonsillitis", 
            "Allergies", 
            "Acid reflux",
            "Viral pharyngitis",
            "Mononucleosis",
            "Environmental irritants"
        ],
        "recommendations": [
            "Gargle with warm salt water", 
            "Stay hydrated with warm liquids", 
            "Use throat lozenges or sprays", 
            "Rest your voice",
            "Use a humidifier",
            "Seek medical attention if severe, persistent, or accompanied by difficulty swallowing or breathing"
        ]
    },
    "back pain": {
        "conditions": [
            "Muscle strain", 
            "Herniated disc", 
            "Sciatica", 
            "Arthritis", 
            "Osteoporosis",
            "Kidney infection",
            "Spinal stenosis",
            "Poor posture"
        ],
        "recommendations": [
            "Apply ice for the first 48-72 hours, then heat", 
            "Take over-the-counter pain relievers if appropriate", 
            "Maintain good posture", 
            "Engage in gentle stretching and strengthening exercises",
            "Avoid heavy lifting",
            "Seek medical attention if pain is severe, radiates down legs, or is accompanied by numbness or weakness"
        ]
    },
    "insomnia": {
        "conditions": [
            "Stress", 
            "Anxiety", 
            "Depression", 
            "Sleep apnea", 
            "Restless leg syndrome",
            "Medication side effect",
            "Caffeine or alcohol consumption",
            "Poor sleep habits"
        ],
        "recommendations": [
            "Establish a regular sleep schedule", 
            "Create a relaxing bedtime routine", 
            "Make your bedroom dark, quiet, and cool", 
            "Limit screen time before bed",
            "Avoid caffeine and alcohol close to bedtime",
            "Consider relaxation techniques like meditation",
            "Seek medical attention if persistent or significantly affecting daily life"
        ]
    },
    "anxiety": {
        "conditions": [
            "Generalized anxiety disorder", 
            "Panic disorder", 
            "Social anxiety disorder", 
            "Phobias", 
            "Post-traumatic stress disorder",
            "Obsessive-compulsive disorder",
            "Medical conditions (thyroid problems, heart arrhythmias)",
            "Medication side effect"
        ],
        "recommendations": [
            "Practice deep breathing and relaxation techniques", 
            "Engage in regular physical activity", 
            "Limit caffeine and alcohol", 
            "Ensure adequate sleep",
            "Consider mindfulness meditation",
            "Seek professional help from a mental health provider if significantly affecting daily life"
        ]
    }
}