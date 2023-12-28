# Ferrous Scrap Price Prediction Model

## Objective

The goal of this project is to develop a robust price prediction model for forecasting three ferrous scrap prices: Busheling CH 10th, Shred CH 10th, and HMS (Heavy Melting Steel) CH 10th.

## Data Source

The dataset comprises monthly records from 2010 to 2023, including key variables classified into supply and demand, macroeconomic indicators, energy prices, and commodities.

## Problem

The aim is to predict market price movements for the three ferrous metals to enhance decision-making.

## Solution

To address this challenge, we propose several modeling approaches:

### Univariate Models
Prophet/ARIMA: Utilize time series forecasting models like Prophet or ARIMA individually for each ferrous scrap type.

### Multivariate Model

Catboost: Employ the Catboost algorithm, a powerful gradient boosting technique, to leverage the interdependencies among the variables.
Combined Models

Prophet X + Prophet Y: Combine univariate Prophet models for different ferrous scrap types.

Prophet X + Catboost Y: Ensemble model combining the strengths of univariate Prophet and multivariate Catboost models.

### Best Results
After rigorous evaluation, the best-performing model is a univariate Prophet/ARIMA with cross-validation, yielding the following metrics:

Mean 1-year monthly RMSE: 88.58

Mean 1-year monthly Accuracy: 53%


## Disclaimer: 

The models are based on historical data, and results may vary due to market dynamics. Regular updates and model retraining are recommended for sustained accuracy.
