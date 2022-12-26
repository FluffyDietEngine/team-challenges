import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd



def first_last_batsman(balls):

    
    balls = balls.sort_values(["id","inning", "over", "ball"], ascending=True)
    first_batsman = (balls['batsman'].iloc[:1]).to_string(index=False)

    print("\n",first_batsman," faced the first ball of IPL \n")

    balls = balls.sort_values(["id","inning", "over", "ball"], ascending=False)
    last_batsman = (balls['batsman'].iloc[:1]).to_string(index=False)

    print(last_batsman," faced the last ball of IPL \n")

def scores(balls):
    
    scores_per_batsman =balls.groupby('batsman').sum()
    df = scores_per_batsman.sort_values(["batsman_runs"], ascending=False)
    hs_batsman = df.iloc[0].name

    print(hs_batsman,"scored highest runs in IPL\n")

    df = scores_per_batsman.sort_values(["batsman_runs"], ascending=True)
    ls_batsman = df.iloc[0].name

    print(ls_batsman,"scored lowest runs in IPL\n")


def total_matches(matches):

    matches["Season"]=pd.DatetimeIndex(matches["date"]).year
    total_matches = matches.groupby(['Season'])['id'].count(). \
                    reset_index().rename(columns={'id':'matches'})
    
    print("Matches played per season")
    print(total_matches,"\n")

def total_runs(matches,balls):

    matches["Season"]=pd.DatetimeIndex(matches["date"]).year
    data = matches[['id', 'Season']].merge(balls, \
                   left_on='id', right_on='id', how='left')
    total_runs = data.groupby(['Season'])['total_runs'].sum().reset_index()

    print("Total runs per season")
    print(total_runs,"\n")

def toss_winners(matches):

    df = matches["toss_winner"].value_counts(ascending=True)
    print("Toss winners of all matches in ascending order")
    print(df)


if __name__ == "__main__":

    balls = pd.read_csv('/home/shrutihande/Downloads/archive/archive/IPL Ball-by-Ball 2008-2020.csv',index_col=False)
    matches = pd.read_csv('/home/shrutihande/Downloads/archive/archive/IPL Matches 2008-2020.csv',index_col=False)

    first_last_batsman(balls)
    scores(balls)
    total_matches(matches)
    total_runs(matches,balls)
    toss_winners(matches)