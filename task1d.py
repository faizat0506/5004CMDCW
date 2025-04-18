import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Load and preprocess data
df = pd.read_csv('Trips_By_Distance.csv')
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')

# 2. Focus on a week with rich data (e.g., Week 32)
df = df[df['Week'] == 32]

# 3. Select features (X) and target (y)
X = df[['Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10',
        'Number of Trips 25-50', 'Number of Trips 50-100']]

y = df['Number of Trips']  # Target: travel frequency in 10–25 mile range

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Drop rows where any element is NaN
X_train = X_train.dropna()
y_train = y_train.loc[X_train.index]  # Make sure y_train matches the new indices

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Mean Squared Error:", mse)
print("R² Score:", r2)
plt.figure(figsize=(12, 6))

# Linear Regression Plot
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)  # Diagonal line
plt.title('Linear Regression: Actual vs Predicted')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
