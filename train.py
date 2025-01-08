import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DEFAULT_FILE_PATH = 'data.csv'
DEFAULT_COEFF_FILE = 'coefficients.csv'
LEARNING_RATE = 0.01
NUM_ITERATIONS = 20000

def load_data(file_path: str = DEFAULT_FILE_PATH) -> tuple[pd.Series, pd.Series]:
    try:
        data = pd.read_csv(file_path)
        if 'km' not in data.columns or 'price' not in data.columns:
            raise ValueError("CSV must contain 'km' and 'price' columns.")

        data = data[['km', 'price']].dropna()
        data = data.astype(float)

        return data['km'], data['price']
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")

def normalize_features(x: pd.Series) -> tuple[pd.Series, float, float]:
    range_x = x.max() - x.min()
    if range_x == 0:
        raise ValueError("Cannot normalize when all values are identical.")
    return (x - x.min()) / (x.max() - x.min()), x.min(), x.max()

def gradient_descent(x: pd.Series, y: pd.Series, learning_rate: float = LEARNING_RATE, 
                    num_iterations: int = NUM_ITERATIONS) -> tuple[float, float, list[float]]:
    theta_0 = 0.0
    theta_1 = 0.0
    m = len(y)
    cost_history = []

    for _ in range(num_iterations):
        predictions = theta_0 + theta_1 * x
        cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
        cost_history.append(cost)

        gradient_0 = (1 / m) * np.sum(predictions - y)
        gradient_1 = (1 / m) * np.sum((predictions - y) * x)

        theta_0 -= learning_rate * gradient_0
        theta_1 -= learning_rate * gradient_1

    return theta_0, theta_1, cost_history

def save_coefficients(theta_0: float, theta_1: float, x_min: float, x_max: float, 
                    file_path: str = DEFAULT_COEFF_FILE) -> None:
    try:
        coefficients = pd.DataFrame({
            'theta_0': [theta_0],
            'theta_1': [theta_1],
            'x_min': [x_min],
            'x_max': [x_max]
        })
        coefficients.to_csv(file_path, index=False)
        print(f"Coefficients saved to {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error saving coefficients: {e}")

def calculate_r_squared(x: pd.Series, y: pd.Series, theta_0: float, theta_1: float) -> float:
    y_pred = theta_0 + theta_1 * x
    sst = np.sum((y - np.mean(y)) ** 2)
    ssr = np.sum((y - y_pred) ** 2)
    r_squared = 1 - (ssr / sst)
    return r_squared

def calculate_mse(y: pd.Series, y_pred: pd.Series) -> float:
    return np.mean((y - y_pred) ** 2)

def calculate_rmse(mse: float) -> float:
    return np.sqrt(mse)

def plot_regression_and_cost(x: pd.Series, y: pd.Series, theta_0: float, theta_1: float, 
                            x_min: float, x_max: float, cost_history: list[float]) -> None:
    try:
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
    except Exception as e:
        print(f"An error occurred during plotting: {e}")

def main():
    try:
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
        print(f"R²: {r_squared:.4f}")
        print(f"MSE: {mse:.4f}")
        print(f"RMSE: {rmse:.4f}")

        plot_regression_and_cost(x, y, theta_0, theta_1, x_min, x_max, cost_history)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
