
import pandas as pd
import numpy as np

df = pd.read_csv('../Dataset/cleaned.csv')

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Scale Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=14)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)


def survived(model, pclass=3, sex=1, age=33, sibsp=1, parch=4):
    # # Feature names (should match training feature names)
#     feature_names = ['pclass', 'sex', 'age', 'sibsp', 'parch']

# # Create input data for prediction
#     x = pd.DataFrame(np.array([[3, 1, 36, 0, 0]]), columns=feature_names)
    x = np.array([[pclass, sex, age, sibsp, parch]]).reshape(1, -1)

    # Apply preprocessing (e.g., scaling)
    x = scaler.transform(x)
    
    # Make predictions
    prediction = model.predict(x)
    probability = model.predict_proba(x)
    
    # Determine the outcome
    if prediction[0] == 0:
        result = "Did not survive"
    else:
        result = "Survived"
    
    # Print the result and probabilities
    print(f"Prediction: {result}")
    print(f"Survival Probability: {probability[0][1]:.2f}")
    print(f"Non-Survival Probability: {probability[0][0]:.2f}")

# Call the function with specific inputs
survived(model, 3, 1, 0, 1, 2)
