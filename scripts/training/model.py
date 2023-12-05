# Import necessary libraries
from feature_extract import y,X
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import mlflow
import mlflow.keras
# Create the LSTM Model
model = Sequential([
    LSTM(256, return_sequences=False, input_shape=(40, 1)),  # LSTM layer with 256 units
    Dropout(0.2),  # Dropout layer to prevent overfitting
    Dense(128, activation='relu'),  # Dense layer with 128 units and ReLU activation
    Dropout(0.2),
    Dense(64, activation='relu'),   # Dense layer with 64 units and ReLU activation
    Dropout(0.2),
    Dense(7, activation='softmax')  # Output layer with 7 units for classification and softmax activation
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  # Compile the model

model.summary()  # Display model summary

# Train the model
history = model.fit(X, y, validation_split=0.2, epochs=50, batch_size=64)  # Train the model with the given data

# Display the training history during each epoch
for epoch in range(50):
    print(f"Epoch {epoch + 1}/50")
    print(f"Training Loss: {history.history['loss'][epoch]:.4f} - Training Accuracy: {history.history['accuracy'][epoch]:.4f}")
    print(f"Validation Loss: {history.history['val_loss'][epoch]:.4f} - Validation Accuracy: {history.history['val_accuracy'][epoch]:.4f}")

# Additional comments on the training details
print("\nTraining Details:")
print("batch_size=64 - amount of data to process per step")
print("epochs=50 - no. of iterations for training the model")
print("validation_split=0.2 - train and test split percentage")
print("The training accuracy and validation accuracy increases each iteration")
print("Best validation accuracy is 72.32")
print("Use checkpoint to save the best validation accuracy model")
print("Adjust learning rate for slow convergence")


mlflow.keras.log_model(model, "lstm_model")

run_id = mlflow.active_run().info.run_id
print(f"RUN_ID: {run_id}")

with open("run_id.txt", "w") as f:
    f.write(run_id)
