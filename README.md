# The Happiness Project

<img width="1117" alt="Screenshot 2024-04-03 at 11 44 23 AM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/fc29c862-78b8-4d8f-a5c0-555f655f7706">

The Happiness Project aims to leverage machine learning techniques to predict an individual's happiness level based on global happiness metrics. By abstracting data from the World Happiness Report to a personal level, this tool offers a unique perspective for self-assessment and understanding happiness determinants.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technical Stack](#dependencies)
- [Installation](#installation)
- [Web Application Overview](#web-application-overview)
- [Usage](#usage)
- [Model Development](#model-development)
- [Collaborators](#collaborators)

## <a id="introduction"></a>Introduction

This project synthesizes data from the World Happiness Report to predict happiness levels on an individual basis. Through exploratory data analysis, model development, and an interactive web interface, users can gain insights into their happiness determinants and see how they compare on a global scale.

### Data Source

The project utilizes the World Happiness Report dataset available on [Kaggle](https://www.kaggle.com/datasets/carlosmorenohernndez/world-happiness-report-2015-2023), which compiles global happiness metrics across several years. This dataset forms the foundation for our analysis and model development, providing a robust framework for understanding the intricacies of happiness on a global scale.

## <a id="project-structure"></a>Project Structure

The repository is organized as follows to ensure ease of navigation and collaboration:

- **`data/`**: Contains all datasets used in the project.
  - `processed/`: Cleaned and processed data ready for modelling.
  - `raw/`: Original datasets.
- **`docs/`**: Documentation related to the project including log of iterative process. 
- **`models/`**: Machine learning models including training and evaluation scripts.
- **`notebooks/`**: Jupyter notebooks for exploratory data analysis and model prototyping.
- **`src/`**: Source code for the application, including Flask backend and frontend assets.
- **`.gitignore`**: Configuration file for ignored files and directories in git.
- **`requirements.txt`**: Required Python libraries for the project.

## <a id="dependencies"></a>Technical Stack

### Data Analysis and Modeling:
- **Pandas:** For data manipulation and analysis.
- **Scikit-learn:** Used for building the machine learning model.

### Backend Framework:
- **Flask:** A lightweight WSGI web application framework.

### Frontend:
- **HTML/CSS:** Basic building blocks of web app interfaces.
- **Bootstrap:** For styling and responsive design.
- **JavaScript:** To add interactivity to the web pages.

### Visualization:
- **Matplotlib/Plotly:** Used for creating static and interactive visualizations.

### Database:
- **SQL Database:** Utilizing SQLite for data storage.
- **SQLAlchemy:** For ORM and database interactions.

### Additional Tools:
- **Pickle:** For loading the trained machine learning model and scaler.
- **NumPy:** For numerical operations on data.
- **Plotly:** For creating interactive plots that can be embedded in the frontend.

## <a id="installation"></a>Installation

To set up your environment to run the project, follow these steps:

1. **Clone the Repository**:  
   `git clone https://github.com/NidaB-C/happiness_project.git`
   
2. **Create a Virtual Environment** (optional, but recommended):  
   `python -m venv venv`  
   `source venv/bin/activate` (Linux/Mac)
   `venv\Scripts\activate` (Windows)
   
4. **Install Dependencies**:  
   `pip install -r requirements.txt`

## <a id="web-application-overview"></a>Web Application Overview

The `app.py` script is the backbone of a Flask web application designed to predict happiness scores based on the World Happiness Report data. It utilizes a machine learning model to forecast an individual's happiness category ('Happy' or 'Not Happy') using various indicators of well-being and national prosperity.

### Features of the Web Application:

- **Model and Scaler Loading:** At startup, the application loads a pre-trained Random Forest machine learning model and a scaler for feature normalization, ensuring that input data is in the correct format for prediction.

- **Data Loading and Database Integration:** The script includes functionality to load processed data into an SQLite database, creating an engine with SQLAlchemy to interact with the database. This allows for the storage and querying of happiness data, which can be utilized for further analysis or to improve model predictions.

- **Prediction Endpoint:** The `/predict` route captures user input from a web form, where users can enter values for GDP per Capita, Social Support, Healthy Life Expectancy, Freedom to Make Life Choices, Perceptions of Corruption, Generosity, and Dystopia Residual. These inputs are then scaled using the loaded scaler and fed into the Random Forest model to predict the happiness category.

- **Result Visualization:** After making a prediction, the application dynamically generates a Plotly graph, comparing the user's input with the global data distribution. This visual representation provides users with a contextual understanding of their predicted happiness score relative to the world.

- **User Input Validation:** The application is designed to handle invalid inputs gracefully, displaying appropriate error messages when non-numeric data is entered.

## <a id="usage"></a>Usage

To use the application and interact with the happiness prediction model:

1. Navigate to the `src/` directory:  
   `cd src/`
   
2. Run the Flask application:  
   `python app.py`
   
3. Open a web browser and go to `http://127.0.0.1:5000/` to interact with the application.

## <a id="model-development"></a>Model Development
### Logistic Regression Model Summary
The Logistic Regression model was evaluated to understand its performance in predicting happiness levels accurately. The model demonstrated exceptional proficiency, as evidenced by its performance metrics, detailed below:

<img width="438" alt="Screenshot 2024-03-27 at 8 26 57 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/251b273e-3018-41ee-8779-30169242e640">

#### Performance Metrics:

- **Accuracy Score**: Achieved an impressive accuracy of 96.78%, indicating a high overall rate of correct predictions across the dataset.

- **Precision**: Exhibited a precision of 98% for classifying individuals as "not happy" and 96% for "happy," suggesting a strong ability to return relevant results.

- **Recall**: Achieved a recall of 96% for the "not happy" class and 98% for the "happy" class, indicating the model's capability to identify all relevant instances effectively.

- **F1-Score**: Both classes observed an F1-score of 97%, showcasing an excellent balance between precision and recall, indicating robust model performance.
  
<img width="497" alt="Screenshot 2024-03-27 at 8 27 31 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/6192b6f7-5c1a-44b4-b66a-c2808add2f50">

#### Confusion Matrix Insights:

- **True Positives (Happy)**: The model correctly identified 165 individuals as happy.
- **True Negatives (Not Happy)**: Accurately classified 166 individuals as not happy.
- **False Positives**: There were 7 instances where individuals were incorrectly predicted as happy.
- **False Negatives**: A small number of 4 individuals were mistakenly classified as not happy.

### Interpretation

The Logistic Regression model's accuracy and balanced precision, recall, and F1-scores across classes illustrate its effectiveness in classifying individuals based on happiness indicators. The model's strength lies in its significant accuracy and the balance between detecting true positives and true negatives while maintaining a low rate of false positives and negatives.

The slight discrepancy between precision and recall in predicting "not happy" vs. "happy" instances points to a marginally higher challenge in classifying "happy" instances with absolute certainty. Nonetheless, the minimal difference does not detract from the model's overall exceptional performance.

This Logistic Regression model's performance marks a promising step towards developing a reliable tool for happiness prediction, offering a solid foundation for further refinement and comparison with other models.

### Decision Tree Model Summary
The exploration of the Decision Tree model for predicting levels of happiness provided valuable insights into its performance. Below is a summary of the key performance metrics observed:

<img width="433" alt="Screenshot 2024-03-27 at 8 55 42 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/8572f8d5-6b5a-42cc-834f-4fd50994ee2e">

#### Performance Metrics:

- **Accuracy Score**: The model recorded an accuracy of 90.05%, indicating a robust ability to make correct predictions across the dataset.

- **Precision**: Showed a precision of 89% for predicting "not happy" and 91% for "happy," reflecting its competence in returning relevant results.

- **Recall**: Demonstrated a recall of 91% for the "not happy" class and 89% for the "happy" class, showcasing the model's capacity to correctly identify nearly all relevant instances.

- **F1-Score**: The F1-scores for both classes were balanced at 90%, signifying a healthy equilibrium between precision and recall, indicative of strong model performance.

<img width="500" alt="Screenshot 2024-03-27 at 8 56 51 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/a8444e87-1af8-442d-b0f6-68af9d75ca1e">

#### Confusion Matrix Insights:

- **True Positives (Happy)**: Effectively identified 150 individuals as happy, showcasing the model's sensitivity.
- **True Negatives (Not Happy)**: Correctly recognized 158 individuals as not happy, highlighting the model's accuracy.
- **False Positives**: Encountered 15 instances of incorrect predictions as happy, suggesting a slight area for improvement.
- **False Negatives**: Reported 19 instances where individuals were mistakenly classified as not happy.

### Interpretation

The Decision Tree model exhibits commendable performance in classifying individuals into happiness categories, with an overall accuracy of 90.05%. Its balanced precision, recall, and F1-scores indicate a capable and reliable model. However, compared to the Logistic Regression and Random Forest models, it shows a slightly higher rate of false positives and negatives, which points towards a margin of improvement in model refinement and feature selection.

The Decision Tree model, with its intuitive understanding and solid performance metrics, stands as an instrumental approach in the project's objective to predict happiness effectively. Continuous refinement and strategic enhancements promise to elevate its predictive accuracy and reliability further.

### Random Forest Model Summary
In our examination of the Random Forest model for predicting happiness levels, the model demonstrated remarkable effectiveness, as evidenced by the collected performance metrics.

<img width="452" alt="Screenshot 2024-03-27 at 8 31 23 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/90313427-3bfa-492a-a8ef-257c0229164f">

#### Performance Metrics:

- **Accuracy Score**: The model achieved an accuracy of 97%, which signifies a high level of correct predictions across the dataset.

- **Precision**: Displayed a precision of 96% for predicting the "not happy" class and an impressive 98% for the "happy" class, indicating a strong propensity to return relevant results.

- **Recall**: Demonstrated a recall of 98% for the "not happy" class and 96% for the "happy" class, underscoring the model’s ability to identify all pertinent instances with minimal errors.

- **F1-Score**: Both classes achieved an F1-score of 97%, indicating an excellent balance between precision and recall, and suggesting a robust performance of the model.

<img width="499" alt="Screenshot 2024-03-27 at 8 52 18 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/7634825b-b9e1-4d57-8536-23a2093b035c">

#### Confusion Matrix Insights:

- **True Positives (Happy)**: Correctly identified 162 individuals as happy, reflecting the model's high sensitivity.
- **True Negatives (Not Happy)**: Accurately classified 169 individuals as not happy, showing the model's precision.
- **False Positives**: A minor count of 4, where individuals were mistakenly predicted as happy.
- **False Negatives**: Recorded a slightly higher count of 7, indicating instances where individuals were wrongly classified as not happy.

### Interpretation

The Random Forest model's near-perfect precision, recall, and F1-scores across both happiness classes highlight its exceptional capability in differentiating between the nuanced states of happiness. Its balanced performance, coupled with a remarkable accuracy score, underscores its effectiveness in classifying individuals accurately.

A slight increase in false negatives compared to the Logistic Regression model indicates a minor challenge in classifying some "happy" instances. However, this slight margin does not significantly detract from the model’s overall impressive performance.

The Random Forest model, with its exceptional accuracy and balanced metrics, stands as a powerful tool for happiness prediction, providing a solid base for further enhancement and ensuring its readiness for deployment.

## Final Model Selection: Random Forest
### Model Selection Rationale

After rigorous evaluation and comparison of three machine learning models—Logistic Regression, Decision Tree, and Random Forest—on our dataset, we have decided to proceed with the Random Forest model for the Global Happiness Predictor application development. This decision is anchored in several critical considerations that highlight the Random Forest model's superiority in terms of accuracy, generalizability, and robustness. Here's why:

### Comparative Analysis

- **Accuracy and Performance**: While all three models demonstrated high levels of accuracy, the Random Forest model emerged slightly superior, exhibiting a balanced precision, recall, and F1-score across both "happy" and "not happy" predictions. It effectively addressed the slight bias in false negatives and false positives observed in the Decision Tree model and matched the Logistic Regression model's performance, making it the most reliable among the three.

- **Handling Complex Relationships**: Unlike the Logistic Regression and Decision Tree models, the Random Forest's ensemble approach enables it to handle complex, nonlinear relationships between features more effectively. This characteristic is crucial for accurately predicting happiness levels, given the multifaceted nature of the factors influencing happiness.

- **Robustness and Generalizability**: The Random Forest model has demonstrated superior robustness and generalizability across various datasets. Its ensemble method, by averaging multiple decision trees, reduces the risk of overfitting—a concern highlighted in the Decision Tree model's perfect accuracy scenario. This makes it exceptionally suited for deployment in a real-world application where data may vary widely.

- **Interpretability and Feature Importance**: While the Decision Tree model scores slightly higher on interpretability due to its simple decision paths, the Random Forest model also offers valuable insights through feature importance scores. These insights can guide further refinement of the app and help understand what drives happiness across populations.

### Moving Forward with Random Forest

Based on the thorough assessment, the Random Forest model stands out as the most appropriate choice for the Global Happiness Predictor application. It strikes an optimal balance between accuracy, interpretability, and the ability to generalize across diverse data sets, ensuring that our application is built on a solid and reliable predictive foundation.

### Next Steps

With the Random Forest model as our selected predictive engine, our next steps will include:

- **Model Tuning and Optimization**: Fine-tuning the Random Forest model to optimize its performance for our specific dataset.
- **Feature Importance Analysis**: Leveraging the Random Forest model's feature importance to gain deeper insights into the factors most predictive of happiness.
- **Integration into the App**: Seamlessly integrating the model into the application architecture to ensure efficient and reliable predictions.
- **Continuous Evaluation and Improvement**: Establishing mechanisms for continuous monitoring and improvement of the model based on user feedback and emerging data.

We are confident that the Random Forest model will empower our application to deliver accurate, insightful, and meaningful predictions of happiness, contributing to a deeper understanding of well-being across different demographics and geographies.

## <a id="collaborators"></a>Collaborators 

- [Sunil Malhi](https://github.com/SunilMalhi)
- [Tafadzwa Fararira](https://github.com/BootcampCoderTF)
- [Yuk Hang Hui](https://github.com/alexyhHui)
- [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)

