# Sentiment Analysis Project

This project performs sentiment analysis on a dataset of customer reviews using VADER sentiment analysis. It includes code to read the dataset, perform sentiment analysis, and visualize the results using bar plots.

![Sentiment Analysis Plot](https://github.com/dkrishnakumar987/SentimentAnalysisPythonScript/blob/main/Sentiment_Analysis.png?raw=true)

## Credits

The dataset used in this project, `Cell_Phones_and_Accessories_5.json`, is sourced from [source](https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews). I would like to express my gratitude to the provider of this dataset for making it available for analysis.

## Features

1. **Data Loading**: The script loads the dataset of customer reviews from the dataset file located in the `data` directory.

2. **Sentiment Analysis**: It performs sentiment analysis on the reviews using the VADER sentiment intensity analyzer to calculate positive, negative, and neutral and compound sentiment scores for each review.

3. **Visualization**: After performing sentiment analysis, the script generates bar plots to visualize the distribution of sentiment scores in the dataset.

## Implementation Details

-   The script uses the `pandas` library to load the dataset and perform data manipulation.
-   It utilizes the `nltk` library for natural language processing and sentiment analysis.
-   The `seaborn` and `matplotlib` libraries are used for data visualization.

## Installation

1. Clone the repository
2. Install the required Python packages using `pip install -r requirements.txt`
3. Download the Dataset from [here](https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews) and extract it in the data directory
4. Ensure the file name is the same as in the script

## Usage

To run the `AnalysisScript.py` file, navigate to the project directory and execute the following command:

```sh
python AnalysisScript.py
```
