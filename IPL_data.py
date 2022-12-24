# python3 ShubhangiLamkhade/friday_challenge.py

import pandas as pd

data_csv1 = pd.read_csv('/home/shubhangi/Downloads/archive (2)/archive/IPL Ball-by-Ball 2008-2020.csv')
# print(data_csv1) 

data_csv2 = pd.read_csv('/home/shubhangi/Downloads/archive (2)/archive/IPL Matches 2008-2020.csv')
# print(data_csv2)

# faced the first in IPL
first_batsman = data_csv1.sort_values(["id","inning", "over", "ball"], ascending=True)
print("first ball faced by:\n\n" ,first_batsman.head(1))

# faced last ball
last_batsman = data_csv1.sort_values(["id","inning", "over", "ball"], ascending=False)
print("Last ball faced by:\n\n" ,last_batsman.head(1))

# Who are the Highest and Lowest run scorers of IPL
data = data_csv1.groupby('batsman').sum()
Highest_scorer = data.sort_values(["batsman_runs"], ascending=False)
print("Highest score Batmans are:\n")
print(Highest_scorer)

scores = data_csv1.groupby('batsman').sum()
Lowest_scorer = scores.sort_values(["batsman_runs"], ascending=True)
print("Lowest score Batmans are:\n")
print(Lowest_scorer)

#Total matches played per season  
clm_add = data_csv2["Seasons"]=pd.DatetimeIndex(data_csv2["date"]).year
total_match_per_season = data_csv2.groupby(['Seasons'])['id'].count().reset_index().rename(columns={'id':'Total_matches'})
print("Tatal matches per season are:\n" ,total_match_per_season)
    

# Total runs scored per season
ball_details = data_csv1
IPL_details = data_csv2[['id', 'Seasons']].merge(ball_details, left_on='id', right_on='id', how='left')
Total_runs = IPL_details.groupby(['Seasons'])['total_runs'].sum().reset_index()
print("\nTotal runs scored per season are:\n" ,Total_runs)

# Toss winners of all matches in ascending order
Toss_winners = data_csv2["toss_winner"].value_counts(ascending=True)
print("\nToss winners are:\n" ,Toss_winners)