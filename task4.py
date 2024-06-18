import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the training data
train_data = pd.read_csv('train.csv')

# Encode the activity labels
label_encoder = LabelEncoder()
train_data['activity'] = label_encoder.fit_transform(train_data['activity'])

# Separate features and target
X = train_data[['tag_identification', 'x', 'y', 'z']]
y = train_data['activity']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest classifier
model = RandomForestClassifier(n_estimators=200, random_state=50)
model.fit(X_train, y_train)

# Load the test data
test_data = pd.read_csv('test.csv')

# Predict the activities for the test data
X_test = test_data[['tag_identification', 'x', 'y', 'z']]
test_data['activity'] = label_encoder.inverse_transform(model.predict(X_test))

# Save the predictions to an output CSV file
output = test_data[['id', 'activity']]
output.to_csv('output.csv', index=False)
