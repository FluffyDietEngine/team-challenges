import pandas as pd

# 1 Total matches played per season

df = pd.read_csv('datasets/IPL Matches 2008-2020.csv')
df['year'] = pd.DatetimeIndex(df['date']).year
df.groupby('year')['year'].count()
'''
output
year
2008    58
2009    57
2010    60
2011    73
2012    74
2013    76
2014    60
2015    59
2016    60
2017    59
2018    60
2019    60
2020    60
'''
########################################################################

# 2 Total runs scored per season

########################################################################

# 3 Toss winners of all matches in ascending order

df = pd.read_csv('datasets/IPL Matches 2008-2020.csv')
df.sort_values(by=['date'], ascending=True)
df['toss_winner']

'''
output
0      Royal Challengers Bangalore
1              Chennai Super Kings
2                 Rajasthan Royals
3                   Mumbai Indians
4                  Deccan Chargers
                  ...             
811                 Mumbai Indians
812                 Delhi Capitals
813            Sunrisers Hyderabad
814                 Delhi Capitals
815                 Delhi Capitals
'''
