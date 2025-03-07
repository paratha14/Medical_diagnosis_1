# Medical Diagnosis Prediction 🩺

Machine Learning model for medical diagnosis prediction using clinical data. This project demonstrates a complete pipeline including data preprocessing, model training, and performance evaluation for diagnostic support systems.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
This repository contains a machine learning solution for medical diagnosis prediction using:
- Dataset: `medical_data.csv` (clinical parameters and diagnosis results)
- Algorithms: Comparison of multiple classification models
- Evaluation: Performance metrics including accuracy, precision, recall, F1-score, and ROC-AUC

## Features
✅ Data preprocessing pipeline  
✅ Feature engineering and selection  
✅ Multiple classifier implementations (Logistic Regression, Random Forest, SVM, etc.)  
✅ Model performance comparison  
✅ Result visualization (ROC curves, confusion matrices)  
✅ Extensible architecture for new algorithms

## Getting Started
### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Virtual environment recommended

### Installation
```bash
# Clone the repository
git clone https://github.com/paratha14/Medical_diagnosis_1.git
cd Medical_diagnosis_1

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
## Results


### Model Performance Comparison
| Model               | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|---------------------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.89     | 0.88      | 0.87   | 0.87     | 0.93    |
| Random Forest       | 0.92     | 0.91      | 0.90   | 0.91     | 0.96    |
| Support Vector Machine | 0.85  | 0.83      | 0.82   | 0.82     | 0.89    |
| XGBoost             | 0.93     | 0.92      | 0.91   | 0.92     | 0.97    |

### Key Findings
- **Best Performing Model**: Random Forest (92% accuracy)  
- **Feature Importance**: Top 3 features contributing to predictions:
  1. Blood Glucose Level (24.5%)
  2. BMI (19.8%)
  3. Age (15.2%)

### Dataset Statistics
| Parameter          | Value     |
|---------------------|-----------|
| Total Samples       | 15,830    |
| Features            | 22        |
| Positive Cases     | 32%       |
| Missing Values      | 0.7%      |

## Contact & Maintainer

### Project Maintainer
**Partha**  
- GitHub: [@paratha14](https://github.com/paratha14)  
- Email: prathammohan3@gmail.com 
- LinkedIn: https://www.linkedin.com/in/pratham-mohan-47013b2b5?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

### Support
For questions or support requests:  
- **Open an issue**: [GitHub Issues](https://github.com/paratha14/Medical_diagnosis_1/issues)  


### Contributing
Contributions are welcome! Please:  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/YourFeature`)  
3. Commit changes (`git commit -m 'Add YourFeature'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a pull request

### License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
