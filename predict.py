import pandas as pd

def load_coefficients(filename='coefficients.csv'):
	try:
		coefficients = pd.read_csv(filename)
		theta_0 = coefficients['theta_0'][0]
		theta_1 = coefficients['theta_1'][0]
		x_min = coefficients['x_min'][0]
		x_max = coefficients['x_max'][0]
	except FileNotFoundError:
		print("Theta file not found. Using default values of 0 for theta_0 and theta_1.")
		theta_0 = 0
		theta_1 = 0
		x_min = 0
		x_max = 1
	return theta_0, theta_1, x_min, x_max

def get_mileage_input():
	while True:
		try:
			mileage = float(input('Enter the mileage of the car: '))
			if mileage < 0:
				print("Mileage cannot be negative. Please enter a positive value.")
			else:
				return mileage
		except ValueError:
			print("Invalid input. Please enter a numeric value for mileage.")

def normalize_input(mileage, x_min, x_max):
	return (mileage - x_min) / (x_max - x_min)

def price_estimation(mileage, theta_0, theta_1):
	return theta_0 + theta_1 * mileage

def main():
	theta_0, theta_1, x_min, x_max = load_coefficients()
	mileage = get_mileage_input()
	mileage_normalized = normalize_input(mileage, x_min, x_max)
	estimated_price = price_estimation(mileage_normalized, theta_0, theta_1)

	print(f"Estimated price for the car: {estimated_price:.2f}")

if __name__ == "__main__":
	main()