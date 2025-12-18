print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("OOB Score:", rf_model.oob_score_)
print(classification_report(y_test, y_pred_rf))
