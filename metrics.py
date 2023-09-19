import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Your input confusion matrix
cm = np.array([[0.25, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.79, 0.00, 0.00, 1.00],
               [0.00, 0.00, 0.00, 0.00, 0.00],
               [0.00, 0.00, 0.00, 0.00, 0.00],
               [0.75, 0.21, 1.00, 1.00, 0.00]])

# Assuming you have a binary threshold to convert the confusion matrix to predictions (0 or 1)
threshold = 0.5
y_pred = (cm >= threshold).astype(int)

# Calculate evaluation metrics
y_true = np.array([0, 1, 0, 0, 1])  # Replace this with your true labels

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
