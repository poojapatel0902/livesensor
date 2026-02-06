# Sensorlive

## Project Objective
The objective of the SensorLive (Sensor Fault Detection) project is to build an end-to-end machine learning system that can automatically detect sensor failures in industrial equipment using historical sensor data.
This helps in predictive maintenance, reducing downtime, preventing unexpected failures, and improving operational efficiency.

## Project Process
The project follows a complete ML pipeline architecture, from data ingestion to deployment:
1. Data Ingestion
Collected sensor data from CSV files
Stored raw data in MongoDB for scalability and persistence
2. Data Validation
Checked schema, column names, and data types
Identified missing values and data inconsistencies
3. Data Transformation
Handled missing values using statistical techniques
Applied feature scaling and encoding
Prepared data for model training
4. Exploratory Data Analysis (EDA)
Analyzed sensor patterns and failure distribution
Detected class imbalance and outliers
5. Model Training
Trained machine learning models to classify Fail / No Fail
Evaluated models using accuracy, precision, recall, and F1-score
6. Model Evaluation & Selection
Compared multiple models
Selected the best-performing model based on evaluation metrics
7. Model Deployment
Saved trained model and preprocessor
Built a REST API using FastAPI for real-time predictions

## Project Insights
Sensor data contains high dimensional features, making preprocessing critical
Class imbalance significantly impacts model performance
Proper data validation prevents pipeline failures
Feature scaling and missing value handling improve prediction accuracy
Automated ML pipelines reduce manual intervention and errors

## Conclusion
The SensorLive project successfully demonstrates how machine learning can be used to detect sensor failures in real time.
By implementing a modular and scalable ML pipeline, the system ensures reliability, maintainability, and production readiness.
This project highlights the practical application of data engineering, machine learning, and deployment in industrial use cases.
