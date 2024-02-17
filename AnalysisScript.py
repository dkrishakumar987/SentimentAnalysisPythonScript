import nltk
import pandas as pd
import seaborn as sns
from tqdm import tqdm
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Overall Rating from Sentiment Score
# Score from -1.0 to 1.0
def SentimentRating(score):
    if score < -0.75:
        return "Very Negative"
    elif score < -0.5:
        return "Negative"
    elif score < -0.25:
        return "Somewhat Negative"
    elif -0.25 < score < 0.25:
        return "Neutral"
    elif score < 0.5:
        return "Somewhat Positive"
    elif score < 0.75:
        return "Positive"
    else:
        return "Very Positive"


# Using ggplot style for GUI
plt.style.use('ggplot')

# Analyzer Object To Perform Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

# Dataset File Path Here
file_path = './data/Cell_Phones_and_Accessories_5.json'
# Column Name Containing Scores/Ratings in Dataset
Scores = 'overall'
# Column Name Containing Review Text in Dataset
TextContent = 'reviewText'

# Reading Dataset(Change this to the specific dataset format)
data = pd.read_json(file_path, lines=True)

df = pd.DataFrame(data)
# Limiting Sample Size to 500
df = df.head(500)


# Perform Sentiment Analysis using VADER on all reviews
result = {}
print("Performing Sentiment Analysis...")
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row[TextContent]
    id = row['reviewerID']
    result[id] = analyzer.polarity_scores(text)

# Converting Result Dict to Dataframe and Merging Dataset with Sentiment Scores
vaders = pd.DataFrame(result).T
vaders = vaders.reset_index().rename(columns={'index': 'reviewerID'})
vaders = vaders.merge(df, how='left', on='reviewerID')

# Creating Subplots
fig, axs = plt.subplots(
    nrows=2, ncols=3, figsize=(
        18, 6), num="Sentiment Analysis")

# Setting Barplot Colors
colors = sns.color_palette("husl", 5)

# Plot 1
sns.barplot(
    data=vaders,
    x=Scores,
    y='neg',
    ax=axs[0][0],
    palette=colors,
    hue=Scores,
    legend=False)
axs[0][0].set_title("Negative Score of Reviews by Stars")
axs[0][0].set_xlabel("Stars")
axs[0][0].set_ylabel("Negative Score")

# Plot 2
sns.barplot(
    data=vaders,
    x=Scores,
    y='neu',
    ax=axs[0][1],
    palette=colors,
    hue=Scores,
    legend=False)
axs[0][1].set_title("Neutral Score of Reviews by Stars")
axs[0][1].set_xlabel("Stars")
axs[0][1].set_ylabel("Neutral Score")

# Plot 3
sns.barplot(
    data=vaders,
    x=Scores,
    y='pos',
    ax=axs[0][2],
    palette=colors,
    hue=Scores,
    legend=False)
axs[0][2].set_title("Positive Score of Reviews by Stars")
axs[0][2].set_xlabel("Stars")
axs[0][2].set_ylabel("Positive Score")

# Plot 4
sns.barplot(
    data=vaders,
    x=Scores,
    y='compound',
    ax=axs[1][0],
    palette=colors,
    hue=Scores,
    legend=False)
axs[1][0].set_title("Compound Score of Reviews by Stars")
axs[1][0].set_xlabel("Stars")
axs[1][0].set_ylabel("Compund Score")

# Plot 5
sns.countplot(
    data=vaders,
    x=Scores,
    ax=axs[1][1],
    palette=colors,
    hue=Scores,
    legend=False)
axs[1][1].set_title("No. of Reviews by Stars")
axs[1][1].set_xlabel("Stars")
axs[1][1].set_ylabel("No. of Reviews")


# Empty Plot
axs[1, 2].set_axis_off()

# Display Average Compound Score
avg_compound_score = vaders['compound'].mean()
print(f"Average Compound Score: {avg_compound_score}")
print(f"Overall Sentiment: {SentimentRating(avg_compound_score)}")

axs[1][2].annotate(
    f"Average Compound Score: {avg_compound_score}\nOverall Sentiment: {SentimentRating(avg_compound_score)}", xy=(
        1.0, -0.2), xycoords='axes fraction', ha='right', va="center", fontsize=10)

# Display Plots
fig.suptitle("Sentiment Analysis Graphs", fontsize=16)
plt.tight_layout()
plt.show()
