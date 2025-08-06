import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
temperature = np.array([22, 20, 18, 23, 30, 32, 29, 26, 24])

coeffs = np.polyfit(time, temperature, 2)
a, b, c = coeffs

def quad(x):
    return a * x**2 + b * x + c

time_fit = np.linspace(0, 24, 100)
temp_fit = quad(time_fit)

plt.scatter(time, temperature, color='blue', label='Observed')
plt.plot(time_fit, temp_fit, color='red', label='Quadratic Fit')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.title('Simple Quadratic Model for Temperature Prediction')
plt.show()

hour = float(input("Enter the hour (0-24) to predict temperature: "))
predicted_temp = quad(hour)
print(f"Predicted temperature at {hour}:00 = {predicted_temp:.2f} °C")
