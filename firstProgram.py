theta_0 = 8249.435532648202
theta_1 = -5330.638795685529

mileage = float(input('Mileage of the car: '))

def priceEstimation(mileage):
	estimatePrice = theta_0 + theta_1 * mileage
	return estimatePrice

estimated_price = priceEstimation(mileage)
print(f"Estimated price for the car: {estimated_price}")