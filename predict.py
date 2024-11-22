import pandas as pd

def load_coefficients(filename='coefficients.csv'):
	try:
		coefficients = pd.read_csv(filename)
		if not all(col in coefficients.columns for col in ['theta_0', 'theta_1', 'x_min', 'x_max']):
			raise ValueError("Invalid file format. Columns 'theta_0', 'theta_1', 'x_min', and 'x_max' are required.")
		theta_0 = coefficients['theta_0'][0]
		theta_1 = coefficients['theta_1'][0]
		x_min = coefficients['x_min'][0]
		x_max = coefficients['x_max'][0]
	except FileNotFoundError:
		print("Theta file not found. Using default values of 0 for theta_0 and theta_1.")
		theta_0, theta_1, x_min, x_max = 0, 0, 0, 1
	except Exception as e:
		print(f"Error loading coefficients: {e}")
		theta_0, theta_1, x_min, x_max = 0, 0, 0, 1
	return theta_0, theta_1, x_min, x_max

def get_mileage_input():
	while True:
		try:
			mileage = float(input('Enter the mileage of the car: '))
			if mileage < 0:
				print("Mileage cannot be negative. Please enter a positive value.")
			elif mileage > 1_000_000:
				print("Mileage seems unrealistically high. Please enter a valid value.")
			else:
				return mileage
		except ValueError:
			print("Invalid input. Please enter a numeric value for mileage.")

def normalize_input(mileage, x_min, x_max):
	if x_min == x_max:
		print("Warning: x_min and x_max are the same. Normalization cannot be performed.")
		return 0
	return (mileage - x_min) / (x_max - x_min)

def price_estimation(mileage: float, theta_0: float, theta_1: float) -> float:
	return theta_0 + theta_1 * mileage

def main():
	theta_0, theta_1, x_min, x_max = load_coefficients()
	mileage = get_mileage_input()
	mileage_normalized = normalize_input(mileage, x_min, x_max)
	estimated_price = price_estimation(mileage_normalized, theta_0, theta_1)

	print(f"Estimated price for the car: {estimated_price:.2f}")

if __name__ == "__main__":
	main()