# ft_linear_regression

![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Docker](https://img.shields.io/badge/docker-20.10%2B-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
	- [Prerequisites](#prerequisites)
	- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)


## Overview

**ft_linear_regression** is a project developed as part of the 42 school curriculum, focusing on implementing linear regression algorithms from scratch. The project emphasizes understanding and applying statistical and machine learning techniques to model and predict data trends.

## Features

- **Linear Regression Model:** Implements a basic linear regression model to predict outcomes based on input features.
- **Data Fitting:** Includes functionality for fitting the model to data, optimizing parameters, and making predictions.
- **Cost Function:** Utilizes cost functions to measure and minimize prediction errors during training.
- **Visualization:** Provides tools to visualize data, regression lines, and model performance.
- **Evaluation Metrics:** Implements evaluation metrics to assess the accuracy and effectiveness of the regression model.

## Architecture

	ft_linear_regression/
	├── README.md
	├── coefficients.csv
	├── data.csv
	├── predict.py
	├── requirements.txt
	└── train.py

## Installation

### Prerequisites


- [Python 3.8+](https://www.python.org/downloads/) installed.
- [Pip](https://pip.pypa.io/en/stable/installation/) installed.
- [Git](https://git-scm.com/) installed.

### Setup

**1. Clone the Repository**

	git clone https://github.com/mdesmartin/ft_linear_regression.git
	cd ft_linear_regression


**2. Create a Virtual Environment**

	python3 -m venv venv
	source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


**3. Install Dependencies**

	pip install -r requirements.txt

## Usage

**1. Train the Model**

	python train.py

This script reads the dataset from data.csv, normalizes the data, trains the linear regression model using gradient descent, and saves the computed coefficients to coefficients.csv.

**2. Predict Prices**

	python predict.py

This script loads the coefficients from coefficients.csv and prompts the user to input a car’s mileage. It then predicts and displays the estimated price based on the trained model.

## Project Structure

**• data.csv:** Dataset containing car mileage and corresponding prices.

**• coefficients.csv:** File where the trained model’s coefficients are saved.

**• train.py:** Script to train the linear regression model.

**• predict.py:** Script to predict car prices based on mileage using the trained model.

**• README.md:** Project documentation.

**• requirements.txt:** List of Python dependencies.

## Technologies

**• Python 3.8+:** Programming language used for development.

**• NumPy:** Library for numerical computations.

**• Pandas:** Data manipulation and analysis library.

**• Matplotlib:** Plotting and visualization library.

## Contribution

Contributions are welcome! Please follow these steps:

1.	Fork the Repository

2.	Create a Feature Branch

		git checkout -b feature/your-feature

3.	Commit Your Changes

		git commit -m "Add your feature"

4.	Push to the Branch

		git push origin feature/your-feature

5.	Open a Pull Request

Ensure your code adheres to project standards and includes appropriate tests.

## License

This project is licensed under the MIT License.

## Contact

**Author:** Mehdi DESMARTIN

**LinkedIn:** linkedin.com/in/mdesmartin

**GitHub:** github.com/mdesmartin