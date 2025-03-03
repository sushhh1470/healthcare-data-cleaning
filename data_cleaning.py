import pandas as pd

# Load the main diabetes dataset
data = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')  # Replace with your main file name

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Fill missing values (if any)
data.fillna(0, inplace=True)  # Replace missing values with 0

# Remove duplicates
data.drop_duplicates(inplace=True)

# Save the cleaned data to a new file
data.to_csv('cleaned_diabetes_data.csv', index=False)

print("\nData cleaning complete! Cleaned data saved as 'cleaned_diabetes_data.csv'.")