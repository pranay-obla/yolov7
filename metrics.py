from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report

# Define the confusion matrix
cm = [[0.00, 0.18, 1.00, 1.00, 0.00],
      [0.00, 0.00, 0.00, 0.00, 0.00],
      [0.00, 0.00, 0.00, 0.00, 0.00],
      [0.00, 0.82, 0.00, 0.00, 1.00],
      [1.00, 0.00, 0.00, 0.00, 0.00]]

# Convert the confusion matrix to integer values (if necessary)
cm = [[int(round(val)) for val in row] for row in cm]
print(cm)

# Extract true labels and predicted labels from the confusion matrix
y_true = []
y_pred = []
for i in range(len(cm)):
    for j in range(len(cm)):
        y_true.extend([i] * cm[i][j])
        y_pred.extend([j] * cm[i][j])
print("True Labels:", y_true)
print("Predicted Labels:", y_pred)

'''
# Calculate various metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

# Print the metrics
print(f"Accuracy: accuracy")
print(f"Precision: precision")
print(f"Recall: recall")
print(f"F1 Score: f1")
'''

# Generate a classification report
target_names = ['Class 0', 'Class 1', 'Class 2', 'Class 3', 'Class 4']
classification_rep = classification_report(y_true, y_pred, target_names=target_names)

print("\nClassification Report:")
print(classification_rep)
