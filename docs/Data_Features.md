# World Happiness Report Data Features

The World Happiness Report dataset provides an exhaustive overview of the state of global happiness. The data encapsulate various metrics that signify the welfare and well-being of populations. Below are the features included in our analysis, extracted from the World Happiness Report, and how they apply to our dataset.

## Features Description

### `Score`
- **Description**: The national average response to the question of life evaluations. It represents the overall happiness level on a scale typically ranging from 0 to 10, with 10 being the highest possible level of happiness.
- **Application**: This is the target variable that we analyse to understand the happiness levels of individuals within the dataset.

### `GDPperCapita`
- **Description**: The extent to which GDP contributes to the calculation of the Happiness Score. It is a measure of a country's economic production that is adjusted for population size.
- **Application**: In our dataset, it serves as a key indicator of the economic dimension of happiness.

### `Family`
- **Description**: The national average of binary responses to the question of whether or not respondents have someone to count on in times of trouble. It reflects the level of social support present within a country.
- **Application**: Used as a proxy for the availability and quality of social support for individuals.

### `LifeExpectancy`
- **Description**: The national average of self-assessed life expectancy. It's a measure of the overall health in the country.
- **Application**: Acts as a feature reflecting the health dimension within our dataset, scaled to be comparable with other metrics.

### `Freedom`
- **Description**: The national average of binary responses to the question of whether respondents feel they are free to make key life choices.
- **Application**: Used to gauge the amount of freedom individuals feel they have in making life choices, a factor known to affect happiness.

### `NoCorruption`
- **Description**: The measure of the absence of corruption, represented by the perceived levels of corruption in government and business.
- **Application**: It captures the trust individuals have in the institutions of their country and the potential impact this has on their happiness.

### `Generosity`
- **Description**: The national average of responses to the question of whether respondents have donated money to a charity in the past month.
- **Application**: Reflects the propensity of individuals to engage in charitable behaviours, a factor that can contribute to a sense of happiness and well-being.

### `DystopiaResidual`
- **Description**: The Dystopia Residual is the residual of the Happiness Score after all the other factors have been taken into account. It represents the unexplained components of happiness.
- **Application**: It serves to capture any discrepancies in happiness not accounted for by the other variables in our model.

## Additional Feature

### `HappinessIndicator`
- **Description**: A binary indicator derived from the Happiness Score that classifies individuals as 'happy' (1) or 'not happy' (0) based on the median score.
- **Application**: Created as part of preprocessing to aid in a binary classification task, it helps to simplify the analysis and modelling of happiness levels.

