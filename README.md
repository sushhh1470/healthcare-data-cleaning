# Healthcare Data Cleaning, Exploration, and Predictive Modeling

This project demonstrates basic data cleaning, exploratory data analysis (EDA), and predictive modeling on the Diabetes Health Indicators Dataset.

## Dataset
The dataset used is the [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) from Kaggle.

## Steps
1. Data Cleaning:
   - Load the dataset.
   - Check for missing values and fill them.
   - Remove duplicates.
   - Save the cleaned dataset as `cleaned_diabetes_data.csv`.

2. Exploratory Data Analysis (EDA):
   - Display dataset information.
   - Visualize the distribution of the target variable (`Diabetes_012`).
   - Create a correlation matrix to understand relationships between variables.
   - Visualize the relationship between BMI and `Diabetes_012`.

3. Predictive Modeling:
   - Build a Random Forest Classifier to predict diabetes.
   - Evaluate the model using accuracy, classification report, and confusion matrix.

## How to Run
1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
## Results

### Data Cleaning
- The dataset was cleaned by handling missing values and removing duplicates.
- The cleaned dataset was saved as `cleaned_diabetes_data.csv`.

### Exploratory Data Analysis (EDA)
1. Distribution of Diabetes_012:
   - The target variable `Diabetes_012` has three classes:
     - `0`: No diabetes (majority class).
     - `1`: Prediabetes (minority class).
     - `2`: Diabetes.
   - The dataset is highly imbalanced, with most samples belonging to the "No diabetes" class.
   - Visualization: `diabetes_distribution.png`.

2. Correlation Matrix:
   - The correlation matrix reveals relationships between variables.
   - Key findings:
     - `BMI` and `Diabetes_012` have a moderate positive correlation.
     - `HighBP` and `Diabetes_012` are also positively correlated.
   - Visualization: `correlation_matrix.png`.

3. BMI vs Diabetes_012:
   - The scatter plot shows the relationship between BMI and diabetes.
   - Key findings:
     - Higher BMI values are associated with a higher likelihood of diabetes (`Diabetes_012 = 2`).
     - Lower BMI values are associated with no diabetes (`Diabetes_012 = 0`).
   - Visualization: `bmi_vs_diabetes.png`.

### Predictive Modeling
- A Random Forest Classifier was trained to predict diabetes.
- The model achieved an accuracy of 0.83 (83%).
- Key Findings:
  - The model performs well for the "No diabetes" class (high precision and recall).
  - It struggles to predict the "Prediabetes" and "Diabetes" classes due to class imbalance.
  - The confusion matrix shows that most misclassifications occur between "No diabetes" and "Diabetes."
- Visualization: `confusion_matrix.png`.

#### Classification Report
          precision    recall  f1-score   support

     0.0       0.85      0.96      0.90     38116
     1.0       0.00      0.00      0.00       906
     2.0       0.46      0.19      0.27      6935

accuracy                           0.83     45957
