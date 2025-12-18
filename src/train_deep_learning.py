start_time = time.time()

history = model_dl.fit(
    X_train_dense,
    y_train,
    epochs=10,
    batch_size=256,
    validation_split=0.1,
    verbose=1
)

training_time = time.time() - start_time
training_time
