
# Predicting GDP per Capita Using Economic Indicators

## Project Description
The primary objective of this project is to develop regression models to predict GDP per Capita using various economic indicators. Data has been collected from over 190 countries, covering a period of 20 years. The analysis focuses on GDP per Capita (US$) as the dependent variable and several other features as independent variables. By leveraging this extensive historical data, we aim to generate insights that are both precise and actionable, enhancing our understanding of economic growth patterns and their driving factors.

## Table of Contents
1. Introduction
2. Objectives
3. Data Collection
4. Data Preparation
5. Exploratory Data Analysis (EDA)
6. Model Development
7. Model Evaluation
8. Results and Discussion
9. Conclusion
10. References

## 1. Introduction
Economic growth is a critical measure of a country’s development. This project aims to understand the factors influencing GDP per Capita and to predict it using various economic indicators through regression modeling.

## 2. Objectives
- To build regression models that accurately predict GDP per Capita.
- To analyze the significance of various economic indicators in predicting GDP per Capita.

## 3. Data Collection
Data is collected from the World Bank Development Indicators, covering over 190 countries for a period of 20 years. The dataset includes the following variables:

## 4. Data Preparation
- Data cleaning and preprocessing
- Handling missing values
- Feature engineering

## 5. Exploratory Data Analysis (EDA)
- Summary statistics
- Visualization of data distributions
- Correlation analysis

## 6. Model Development
- Multiple Linear Regression
- Lasso Regression
- Elastic Net Regression
- Ridge Regression

## 7. Model Evaluation
- Performance metrics: R-squared, Root Mean Squared Error (RMSE)
- Cross-validation
- Model comparison

## 8. Results and Discussion
- Interpretation of model coefficients
- Importance of various predictors
- Insights and implications

## 9. Conclusion
- Summary of findings
- Implications for economic policy

## 10. References
- World Bank Development Indicators
- Relevant academic papers and articles

## Variable Descriptions

| Variable Name       | Description                                               |
|---------------------|-----------------------------------------------------------|
| GDP_per_Capita      | Gross Domestic Product per Capita (US$)                   |
| Trade_Rate          | Trade as a percentage of GDP                              |
| Labor_Force         | Total labor force of the country                          |
| Population          | Total population of the country                           |
| Industrial_Construction | Investment in industrial construction (US$)              |
| Year                | Year of observation                                       |
| Country             | Country name                                              |

## How to Run the Project
1. Clone the repository.
2. Ensure you have the necessary libraries installed (e.g., pandas, numpy, sklearn, matplotlib).
3. Run the Jupyter notebooks in the following order:
   - `transform_and_eda.ipynb`
   - `model_development.ipynb`
   - `models_With_Cross_Validation.ipynb`

4. Follow the steps outlined in each notebook for data preprocessing, modeling, and evaluation.

## Requirements
- Python 3.x
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- matplotlib
- Excel

## Author
Ismael Bah

---


