from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, preds),
        "f1_macro": f1_score(y_test, preds, average='macro'),
        "confusion_matrix": confusion_matrix(y_test, preds)
    }
