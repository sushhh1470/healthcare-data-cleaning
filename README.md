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
- The cleaned data is saved as `cleaned_diabetes_data.csv`.
- The distribution of the target variable (`Diabetes_012`) is saved as `diabetes_distribution.png`.
- The correlation matrix is saved as `correlation_matrix.png`.
- The relationship between BMI and `Diabetes_012` is saved as `bmi_vs_diabetes.png`.
-The confusion matrix for the predictive model is saved as confusion_matrix.png.
