baseline_model = LogisticRegression(max_iter=1000)

baseline_model.fit(X_train, y_train)

y_pred_baseline = baseline_model.predict(X_test)
