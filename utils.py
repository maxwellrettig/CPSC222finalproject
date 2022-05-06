import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

# loading the json into a pandas dataframe
stats_df = pd.read_json("spotify_hist.json")
# deleting songs with 0ms listened to
stats_df = stats_df.loc[~(stats_df == 0).any(axis=1)]

def longest_song(stats_df):
    # finding the longest song
    longest_song = max(stats_df["msPlayed"])
    longest_song /= 60000.0
    print("Longest song:", round(longest_song, 2), "minutes")

def histogram_chart_example(x_ser):
    plt.figure()
    plt.hist(x_ser)

def hypothesis_test(artist_df):
    t, pval = stats.ttest_1samp(artist_df["msPlayed"], 120000)
    alpha = 0.05
    pval /= 2 # divide by two because 1 rejection region

    if pval < alpha:
        print("Reject H0")
    else:
        print("Do not reject H0")