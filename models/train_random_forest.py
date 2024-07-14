from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import pickle

# Load the dataset
data_cleaned = pd.read_csv('../data/processed/cleaned_happiness_data.csv')

# Define features and target variables
features = data_cleaned.drop(['HappinessIndicator', 'Score'], axis=1)
target = data_cleaned['HappinessIndicator']

# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=78)

# Scale the features - Adjusted to fit the scaler on the training data only, then transform both training and test sets
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit and transform training data
X_test_scaled = scaler.transform(X_test)        # Transform test data based on the scaler fitted on the training data

# Save the scaler for future use, considering naming consistency
with open('../models/scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Create the Random Forest classifier instance and fit the model on the scaled training data
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Save the Random Forest model
with open('../models/random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(rf_model, model_file)
