# Credit Card Fraud Detection using Machine Learning

## ABSTRACT
Credit card fraud is a significant problem, with billions of dollars lost each year. Machine learning can be used to detect credit card fraud by identifying patterns that are indicative of fraudulent transactions. Credit card fraud refers to the physical loss of a credit card or the loss of sensitive credit card information. Many machine learning algorithms can be used for detection. This project proposes to develop a machine-learning model to detect credit card fraud. The model will be trained on a dataset of historical credit card transactions and evaluated on a holdout dataset of unseen transactions.

**Keywords:** Credit Card Fraud Detection, Fraud Detection, Fraudulent Transactions, K-Nearest Neighbors, Support Vector Machine, Logistic Regression, Decision Tree.

## Overview
With the increase of people using credit cards in their daily lives, credit card companies should take special care of the security and safety of the customers. According to (Credit card statistics 2021), the number of people using credit cards worldwide was 2.8 billion in 2019; also, 70% of those users own a single card. Reports of Credit card fraud in the U.S. rose by 44.7% in 2020. There are two kinds of credit card fraud, and the first is having a credit card account opened under your name by an identity thief. Reports of this fraudulent behaviour increased 48% in 2020. The second type is when an identity thief uses an existing account you created, usually by stealing the information on the credit card. Reports on this type of Fraud increased 9% in 2020 (Daly, 2021). Those statistics caught our attention as the numbers have increased drastically and rapidly throughout the years, which motivated us to resolve the issue analytically by using different machine learning methods to detect fraudulent credit card transactions within numerous transactions.

## Project Goals
The main aim of this project is the detection of fraudulent credit card transactions, as it is essential to figure out the fraudulent transactions so that customers do not get charged for the purchase of products that they did not buy. Fraudulent Credit card transactions will be detected with multiple ML techniques. Then, a comparison will be made between the outcomes and results of each method to find the best and most suited model for detecting fraudulent credit card transactions; graphs and numbers will also be provided. In addition, it explores previous literature and different techniques used to distinguish Fraud within a dataset.

## Features
- Preprocessing of an imbalanced dataset using SMOTE (Synthetic Minority Oversampling Technique).
- Implementation of feature scaling to normalize data.
- Application of Logistic Regression and Random Forest algorithms for classification.
- Performance evaluation using metrics like recall, AUC-ROC, precision, and confusion matrices.
- Visualization of results and insights using Matplotlib and Seaborn.

## Tools and Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Imbalanced-learn

## Workflow
1. **Data Preprocessing:**
   - Handled missing values and duplicates.
   - Used SMOTE to balance the dataset.
   - Applied feature scaling for better model performance.
2. **Feature Engineering:**
   - Selected relevant features for model training.
3. **Model Training:**
   - Trained models using Logistic Regression and Random Forest algorithms.
   - Tuned hyperparameters for optimal performance.
4. **Model Evaluation:**
   - Evaluated models using recall, precision, AUC-ROC, and confusion matrices.
   - Focused on achieving a high recall score to reduce false negatives.

## Results
- The Random Forest model achieved high recall and AUC-ROC scores, making it the preferred model for deployment.

## Deployment
The project is deployed on **Render**, enabling real-time fraud detection capabilities.

## How to Run
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd credit-card-fraud-detection
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```bash
   python app.py
   ```

## Repository Structure
```
.
|-- data/                # Contains the dataset (not included for confidentiality)
|-- models/              # Saved machine learning models
|-- notebooks/           # Jupyter notebooks for analysis and experimentation
|-- app.py               # Main application script
|-- requirements.txt     # List of dependencies
|-- README.md            # Project documentation
```

## Future Improvements
- Incorporate additional features to enhance model accuracy.
- Explore other machine learning models, such as Gradient Boosting.
- Integrate the project with a real-time transaction monitoring system.

## Contact
If you have any questions or suggestions, feel free to contact me:
- **Email:** [your_email@example.com]
- **LinkedIn:** [your_linkedin_profile]

---

### Note:
The dataset used in this project is anonymized and was obtained from [Kaggle's Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).
