Ferrous Scrap Price Prediction Model

Objective
The goal of this project is to develop a robust price prediction model for forecasting three ferrous scrap prices: Busheling CH 10th, Shred CH 10th, and HMS (Heavy Melting Steel) CH 10th.

Data Source
The dataset comprises monthly records from 2010 to 2023, including key variables classified into supply and demand, macroeconomic indicators, energy prices, and commodities.

Problem
The aim is to predict market price movements for the three ferrous metals to enhance decision-making.

Solution
To address this challenge, we propose several modeling approaches:

Univariate Models
Prophet/ARIMA: Utilize time series forecasting models like Prophet or ARIMA individually for each ferrous scrap type.
Multivariate Model
Catboost: Employ the Catboost algorithm, a powerful gradient boosting technique, to leverage the interdependencies among the variables.
Combined Models
Prophet X + Prophet Y: Combine univariate Prophet models for different ferrous scrap types.
Prophet X + Catboost Y: Ensemble model combining the strengths of univariate Prophet and multivariate Catboost models.
Best Results
After rigorous evaluation, the best-performing model is a univariate Prophet/ARIMA with cross-validation, yielding the following metrics:

Mean 1-year monthly RMSE: 88.58
Mean 1-year monthly Accuracy: 53%
Implementation Guide (GitHub Readme)
Repository Structure
Code: Contains implementation scripts for each modeling approach.
Data: Store the raw data and any preprocessed datasets.
Results: Document the model outputs, including metrics, visualizations, and comparisons.
Instructions for Running Models
Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Follow the specific instructions in each model's script within the "Code" directory.
Model Selection
Choose the appropriate model based on your preference for accuracy, interpretability, or computational efficiency.
Consider the ensemble model for a balanced approach.
Evaluation
Refer to the "Results" directory for detailed evaluations and comparisons.
Assess the model performance based on RMSE and accuracy metrics.
Future Work
Explore additional feature engineering techniques for improved model performance.
Experiment with alternative algorithms to further enhance prediction accuracy.
Feel free to reach out for any questions or support!

Disclaimer: The models are based on historical data, and results may vary due to market dynamics. Regular updates and model retraining are recommended for sustained accuracy.
