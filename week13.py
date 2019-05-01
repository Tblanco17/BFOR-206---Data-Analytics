import pandas as pd
import nltk
from scipy import stats

trial_data = pd.read_csv('/home/tyler/scripts/trial_data.csv')

trial_data['totalwords'] = trial_data['transcript'].str.split().str.len()

words_bycond = trial_data.groupby('condition')['transcript'].apply(lambda x: ''.join(x))

words_bycond = trial_data.groupby('condition')['transcript'].apply(lambda x: '|'.join(x))

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk_sentiment = SentimentIntensityAnalyzer()

full_sent = trial_data['transcript'].apply(lambda x:nltk_sentiment.polarity_scores(x))

trial_data['sentiment'] = full_sent.apply(lambda x: x['compound'])

print(trial_data['sentiment'].head())

lies = trial_data[trial_data['condition']=='lie']
truth = trial_data[trial_data['condition']=='truth']

trial_data.groupby('condition')['sentiment'].mean()
stats.ttest_ind(lies['sentiment'], truth['sentiment'])

most_positive = trial_data.loc[trial_data['sentiment'].idxmax()]
print(most_positive['transcript'])
most_negative = trial_data.loc[trial_data['sentiment'].idxmin()]
print(most_negative['transcript'])
