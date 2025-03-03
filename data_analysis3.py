import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
data = pd.read_csv('cleaned_diabetes_data.csv')

# Display basic descriptive statistics
print("Descriptive Statistics:")
print(data.describe())




# Visualize the relationship between BMI and Diabetes_012
plt.figure(figsize=(8, 6))
sns.scatterplot(x='BMI', y='Diabetes_012', data=data)
plt.title('BMI vs Diabetes_012')
plt.xlabel('BMI')
plt.ylabel('Diabetes_012')
plt.savefig('bmi_vs_diabetes.png')  # Save the plot as an image
plt.show()