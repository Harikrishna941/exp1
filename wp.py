import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

days = np.array([1, 2, 3, 4, 5, 6, 7])
temps = np.array([30, 32, 35, 33, 36, 38, 37])

coeffs = np.polyfit(days, temps, 2)
a, b, c = coeffs
print(f"Fitted Quadratic Equation: T(d) = {a:.3f}*d^2 + {b:.3f}*d + {c:.3f}")

predicted_temps = a * days**2 + b * days + c

mse = mean_squared_error(temps, predicted_temps)
print(f"Mean Squared Error: {mse:.3f}")

plt.scatter(days, temps, color='blue', label='Actual Data')
plt.plot(days, predicted_temps, color='red', label='Quadratic Fit')
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Quadratic Temperature Prediction")
plt.legend()
plt.grid(True)
plt.show()

future_days = np.array([8, 9, 10])
future_predictions = a * future_days**2 + b * future_days + c

for day, temp in zip(future_days, future_predictions):
    print(f"Predicted Temperature on Day {day}: {temp:.2f}°C")
