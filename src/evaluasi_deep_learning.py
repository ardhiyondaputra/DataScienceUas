y_pred_dl = (model_dl.predict(X_test_dense) > 0.5).astype("int")

print("Accuracy:", accuracy_score(y_test, y_pred_dl))
print(classification_report(y_test, y_pred_dl))
