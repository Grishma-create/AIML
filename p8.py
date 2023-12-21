from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load Iris dataset and split into training and testing sets
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)

# Predict and print results for each test sample
predictions = knn.predict(X_test)
for actual, predicted in zip(y_test, predictions):
    print(f"Actual: {iris.target_names[actual]}, Predicted: {iris.target_names[predicted]}")

# Print test accuracy score
print(f"\nTest Score (Accuracy): {knn.score(X_test, y_test):.2f}\n")
