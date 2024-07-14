from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# Load the scaler and model
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))
rf_model = pickle.load(open('../models/random_forest_model.pkl', 'rb'))

# Load the dataset
data_cleaned = pd.read_csv('../data/processed/cleaned_happiness_data.csv')

# Define features and target
features = data_cleaned.drop(['HappinessIndicator', 'Score'], axis=1)
target = data_cleaned['HappinessIndicator']

# Split the data 
X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=78)

# Scale the features AFTER splitting (important change)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Making predictions using the SCALED test data
rf_predictions = rf_model.predict(X_test_scaled)

# Calculating the confusion matrix and accuracy score
rf_cm = confusion_matrix(y_test, rf_predictions)
rf_cm_df = pd.DataFrame(
    rf_cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
)
acc_score = accuracy_score(y_test, rf_predictions)

# Displaying results
print("Confusion Matrix")
print(rf_cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification Report")
print(classification_report(y_test, rf_predictions))

# Generate and display the confusion matrix using seaborn
sns.heatmap(rf_cm_df, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
