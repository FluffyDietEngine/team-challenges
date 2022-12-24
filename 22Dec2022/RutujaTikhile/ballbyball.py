import pandas as pd

# 1 Who faced the first and last ball in IPL?

data = pd.read_csv("datasets/IPL Ball-by-Ball 2008-2020.csv")
df = pd.read_csv('datasets/IPL Matches 2008-2020.csv')

# reading two csv files
data1 = pd.read_csv('datasets/IPL Ball-by-Ball 2008-2020.csv')
data2 = pd.read_csv('datasets/IPL Matches 2008-2020.csv')

# using merge function by setting how='inner'
output1 = pd.merge(data1, data2, on='id', how='inner')
  
# displaying result
print(output1.head(5))
output1.to_csv('file1.csv')
df_new = pd.read_csv('file1.csv')
df_new['date'].agg(['min', 'max'])
# min   2008-04-18 first day of match
# max   2020-11-10 last day of match
# que quit
##########################################################################

# 2 Who are the Highest and Lowest run scorers of IPL?
df = pd.read_csv('datasets/IPL Ball-by-Ball 2008-2020.csv')
df = df.groupby(['batsman'], as_index=False)['total_runs'].sum()
df['total_runs'].agg(['min', 'max'])
'''
output
min       0
max    6081
'''

idx = df.index[df['total_runs']==6081]
Highest_run = df.loc[idx]
'''
output
     batsman  total_runs
505  V Kohli        6081
'''
idx = df.index[df['total_runs']==0]
Lowest_run = df.loc[idx]
'''
output
            batsman  total_runs
58     Abdur Razzak           0
64   Arshdeep Singh           0
91          C Nanda           0
139         DR Sams           0
178       IC Pandey           0
204        JL Denly           0
228        KK Ahmed           0
246        L Ablish           0
321        ND Doshi           0
387      RR Bhatkal           0
411       S Kaushik           0
413    S Lamichhane           0
457     SS Cottrell           0
479     Sunny Gupta           0
499          U Kaul           0
506  V Pratap Singh           0
526   Y Prithvi Raj           0
'''
