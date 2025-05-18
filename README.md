# SymptomAnalyzer

A diagnostic tool that allows users to input symptoms and receive potential conditions and recommendations for further action, powered by advanced natural language processing.

## Features

- **Symptom Analysis**: Enter symptoms to receive potential conditions
- **Severity Assessment**: Color-coded severity levels (Emergency, Urgent, Moderate, Mild)
- **Related Symptoms**: Suggestions for related symptoms to improve diagnosis accuracy
- **Recommendations**: Actionable advice based on symptom severity

## Technology Stack

- **Backend**: Flask with Python
- **Frontend**: HTML, CSS, JavaScript with Bootstrap
- **Data**: Comprehensive medical knowledge database

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install flask flask_cors
   ```
3. Run the application:
   ```
   python app.py
   ```

## Usage

1. Enter symptoms separated by commas (e.g., "headache, fever, cough")
2. Click "Analyze Symptoms"
3. View results including potential conditions, severity, and recommendations
4. Explore related symptoms by clicking on the suggested buttons

## Disclaimer

This tool is for informational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.

## License

MIT