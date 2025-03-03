# Healthcare Data Cleaning and Exploration 
This project demonstrates basic data cleaning and exploration on the Diabetes Health Indicators Dataset. 
ECHO is on.
## Dataset 
The dataset used is the [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) from Kaggle. 
ECHO is on.
## Steps 
1. Load the dataset. 
2. Check for missing values and fill them. 
3. Remove duplicates. 
4. Perform exploratory data analysis (EDA): 
   - Display dataset information. 
   - Visualize the distribution of the target variable (\`Diabetes_012\`). 
   - Display summary statistics for numerical columns. 
5. Save the cleaned data. 
ECHO is on.
## How to Run 
1. Clone this repository. 
2. Install the required libraries: 
\`\`\`bash 
pip install pandas numpy matplotlib seaborn 
\`\`\` 
3. Run the script: 
\`\`\`bash 
python data_cleaning.py 
\`\`\` 
ECHO is on.
## Results 
## Results
- The cleaned data is saved as `cleaned_diabetes_data.csv`.
- The distribution of the target variable (`Diabetes_012`) is saved as `diabetes_distribution.png`.
- The correlation matrix is saved as `correlation_matrix.png`.
- The relationship between BMI and `Diabetes_012` is saved as `bmi_vs_diabetes.png`.
