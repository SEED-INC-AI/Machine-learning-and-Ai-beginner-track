import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(train.head())


print("\nChecking for missing values:")
print(train.isnull().sum())


train['price_range'] = train['price_range'].apply(lambda x: 0 if x <= 1 else 1)

print("\nNew price categories:")
print(train['price_range'].value_counts())


X = train.drop("price_range", axis=1)
y = train["price_range"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)


test_features = test.drop("id", axis=1)

test_predictions = model.predict(test_features)

print("\nTest Predictions:")
print(test_predictions[:10])


output = pd.DataFrame({
    "Prediction": test_predictions
})

output.to_csv("predictions.csv", index=False)

print("\nPredictions saved to predictions.csv")