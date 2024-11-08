# Student Response Analysis

This project analyzes student response data from 2021 and 2022 to gain insights into student performance, question difficulty, and to build a predictive model for correct responses.

## Project Structure

```

├── data/
│   ├── student_responses_2021.csv       # Raw data file for 2021
│   └── student_responses_2022.csv       # Raw data file for 2022
├── main/
│   ├── app.py                           # Main application script
│   └── streamlit.py                     # Streamlit application for interactive exploration
├── model/
│   └── best_model.pkl                   # Saved model for predicting correct responses
├── notebooks/
│   └── analysis.ipynb                   # Jupyter notebook for detailed EDA and modeling
├── reports/                             # Directory for generated reports and visualizations
├── requirements.txt                     # Dependencies for the project
└── README.md                            # Project documentation (this file)
```
Project Overview
```
The main objectives of this project are to:

Analyze student response data to identify changes in student ability and question difficulty over time.
Build a predictive model to determine whether a student will answer a question correctly.
Provide interactive visualizations and insights using Streamlit.
```
Data Description
```
The project uses two CSV files representing student responses in 2021 and 2022:

student_id: Unique identifier for each student.
question_id: Unique identifier for each question.
ability: A measure of the student's skill level.
difficulty: A measure of the question's difficulty.
answered_correctly: Indicates if the student answered the question correctly (True/False).
year: Added to distinguish responses from 2021 and 2022 after merging the datasets.

```
Installation
```
To run this project locally, follow these steps:

1. Clone the repository:
git clone https://github.com/VishalSharmaDataScience/student_response_app/tree/version-1
cd student_response_app

2. Set up a virtual environment (recommended):

python3 -m venv .venv
source .venv/bin/activate

3. Install the required dependencies:
pip install -r requirements.txt

```
Usage
```
Exploratory Data Analysis (EDA)
You can explore the data and perform EDA by running the Jupyter notebook located in notebooks/analysis.ipynb. The notebook provides insights into:

Changes in student ability and question difficulty over time.
Distribution of scores and the frequency of correct responses.
Outlier detection and handling.
```
Streamlit Application
```
For an interactive experience, use the Streamlit application:
streamlit run main/streamlit.py
```
Predictive Model
```
The predictive model is built and saved as best_model.pkl in the model directory. This model predicts whether a student will answer a question correctly based on:

1. Student's ability.
2. Question difficulty.
3. Year

```
Key Findings
```
Ability and Difficulty Trends: Analyzed trends in student ability and question difficulty over time, revealing patterns in performance and question complexity.
Predictive Model: A model was trained to predict correct answers, achieving satisfactory accuracy (details in analysis.ipynb).
Additional Observations: Notable patterns in student responses, possible biases, and outlier impacts.

```
Future Improvements
```
AI Agents for Automation: Integrate AI agents for automated data processing, EDA, and model tuning.
Use of LLMs for Insights: Leverage large language models (LLMs) to automatically generate summaries and insights based on analysis.
Continuous Model Improvement: Set up a pipeline for retraining the model with new data, enabling adaptive learning.
```
Contributing
```
Contributions are welcome! Please open an issue or submit a pull request if you have ideas for improvement.




