import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path='data.csv'):
	data = pd.read_csv(file_path)
	x = data['km'].astype(float)
	y = data['price'].astype(float)
	return x, y

def normalize_features(x):
	return (x - x.min()) / (x.max() - x.min()), x.min(), x.max()

def gradient_descent(x, y, learning_rate=0.01, num_iterations=20000):
	theta_0 = 0.0
	theta_1 = 0.0
	m = len(y)
	cost_history = []

	for i in range(num_iterations):
		predictions = theta_0 + theta_1 * x
		cost = (1/(2*m)) * np.sum((predictions - y) ** 2)
		cost_history.append(cost)

		gradient_0 = (1/m) * np.sum(predictions - y)
		gradient_1 = (1/m) * np.sum((predictions - y) * x)

		theta_0 -= learning_rate * gradient_0
		theta_1 -= learning_rate * gradient_1

	return theta_0, theta_1, cost_history

def save_coefficients(theta_0, theta_1, x_min, x_max, file_path='coefficients.csv'):
	coefficients = pd.DataFrame({
		'theta_0': [theta_0],
		'theta_1': [theta_1],
		'x_min': [x_min],
		'x_max': [x_max]
	})
	coefficients.to_csv(file_path, index=False)
	print(f"Coefficients saved to {file_path}")

def calculate_r_squared(x, y, theta_0, theta_1):
	y_pred = theta_0 + theta_1 * x
	sst = np.sum((y - np.mean(y)) ** 2)
	ssr = np.sum((y - y_pred) ** 2)
	r_squared = 1 - (ssr / sst)
	return r_squared

def calculate_mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)

def calculate_rmse(mse):
    return np.sqrt(mse)

def plot_regression_and_cost(x, y, theta_0, theta_1, x_min, x_max, cost_history):
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

	denormalized_theta_1 = theta_1 / (x_max - x_min)
	denormalized_theta_0 = theta_0 - denormalized_theta_1 * x_min

	ax1.scatter(x, y, color='blue', label='Original data')

	regression_line = denormalized_theta_0 + denormalized_theta_1 * x
	ax1.plot(x, regression_line, color='green', label='Linear regression')

	ax1.set_xlabel('Mileage')
	ax1.set_ylabel('Price')
	ax1.set_title('Mileage vs Price with Linear Regression')
	ax1.legend()

	ax2.plot(range(len(cost_history)), cost_history, color='green')
	ax2.set_xlabel('Iteration')
	ax2.set_ylabel('MSE')
	ax2.set_title('Mean Squared Error over Iteration')

	plt.tight_layout()
	plt.show()

def main():
	x, y = load_data()
	x_normalized, x_min, x_max = normalize_features(x)

	theta_0, theta_1, cost_history = gradient_descent(x_normalized, y)
	save_coefficients(theta_0, theta_1, x_min, x_max)

	y_pred = theta_0 + theta_1 * x_normalized
	r_squared = calculate_r_squared(x_normalized, y, theta_0, theta_1)
	mse = calculate_mse(y, y_pred)
	rmse = calculate_rmse(mse)

	print(f"theta_0: {theta_0}")
	print(f"theta_1: {theta_1}")
	print(f"R²: {r_squared}")
	print(f"MSE: {mse}")
	print(f"RMSE: {rmse}")

	plot_regression_and_cost(x, y, theta_0, theta_1, x_min, x_max, cost_history)


if __name__ == "__main__":
	main()
