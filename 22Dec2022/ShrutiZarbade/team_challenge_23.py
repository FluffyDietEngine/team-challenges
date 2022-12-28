""" This file is having 5 different Function built over Pandas Library
    Author : Shruti Zarbade
    Date : 23 Dec 2022
"""
import pandas as pd


def first_last_ball():
    """
    This function will find a batsman who faced the first and last ball in IPL
    """
    df = pd.read_csv("IPL-Ball-by-Ball 2008-2020.csv")
    match_id = df.sort_values("id")
    sorted_values = match_id.sort_values(
        ["inning", "over", "ball"], ascending=[True, True, True]
    )

    # first ball
    first_ball = sorted_values.head(1)
    index_ = first_ball.index.values[0]
    first_ball = first_ball._get_value(index_, "batsman")

    # last ball
    last_ball = sorted_values.tail(1)
    ball_index = last_ball.index.values[0]
    last_ball = last_ball._get_value(ball_index, "batsman")

    data = [["faced_first_ball", first_ball], ["faced_last_ball", last_ball]]
    df_ = pd.DataFrame(data, columns=["ball", "batman_name"])
    df_.to_csv("faced_first_last_ball.csv", index=False)


def higest_lowest_runs():
    """
    This Function will find the batsman name and runs
    who scores highest and the lowest runs in the IPL
    """
    df = pd.read_csv("IPL-Ball-by-Ball 2008-2020.csv")
    df2 = df.groupby(["batsman"]).sum()

    # Highest Score
    high_ = df2.nlargest(1, ["total_runs"])
    high = high_.loc[:"batsman", "total_runs"]

    # Lowest Score
    low_ = df2.nsmallest(1, ["total_runs"])
    low = low_.loc[:"batsman", "total_runs"]

    data = [
        ["Highest_Score", high.index[0], high.values[0]],
        ["Lowest_Score", low.index[0], low.values[0]],
    ]

    dataframe = pd.DataFrame(data, columns=["category", "batsman", "runs"])
    dataframe.to_csv("highest_lowest_score.csv", index=False)


def total_matches_in_season():
    """This method will provide you the number of
    matches played per season.."""
    df = pd.read_csv("IPL Matches 2008-2020.csv")
    df["year"] = pd.DatetimeIndex(
        df["date"]
    ).year  # returning the year from date format
    list_ = []
    for dt_ in range(2008, 2021):
        no_matches = df["year"].value_counts()[dt_]
        list_.append([dt_, no_matches])

    dataframe = pd.DataFrame(list_, columns=["year", "no of matches played"])
    dataframe.to_csv("no_matches_played.csv", index=False)


def total_run_score_season():
    """
    This method will give you the total run score
    in every season.
    """

    # getting total number of runs per match id
    df = pd.read_csv("IPL-Ball-by-Ball 2008-2020.csv")
    df2 = df.groupby(["id"])
    total = df2["total_runs"].sum()

    # getting match id per season
    df_ = pd.read_csv("IPL Matches 2008-2020.csv")
    df2_ = df_.groupby(["date", "id"])
    total_ = df2_["result_margin"].sum()

    pd.merge(total, total_).to_csv("total_run_score.csv", index=False)


def toss_winner_all_matches():
    """
    This method will find the toss winner of
    all matches held between 2008-2020
    """
    df = pd.read_csv("IPL Matches 2008-2020.csv")
    sort_values = df.sort_values(["id", "date"], ascending=True)
    df2 = sort_values[["id", "date", "toss_winner"]]
    df2.to_csv("toss_winner.csv", index=False)


if __name__ == "__main__":

    first_last_ball()
    higest_lowest_runs()
    total_matches_in_season()
    total_run_score_season()
    toss_winner_all_matches()
