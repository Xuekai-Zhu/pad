def solution():
    total_toothbrushes = 330  # Dr. Banks had 330 toothbrushes to give away
    given_away_jan = 53
    given_away_feb = 67
    given_away_mar = 46

    remaining_toothbrushes = total_toothbrushes - given_away_jan - given_away_feb - given_away_mar
    given_away_apr = remaining_toothbrushes / 2
    given_away_may = remaining_toothbrushes / 2

    busiest_month = max(given_away_jan, given_away_feb, given_away_mar, given_away_apr, given_away_may)
    slowest_month = min(given_away_jan, given_away_feb, given_away_mar, given_away_apr, given_away_may)

    more_toothbrushes = busiest_month - slowest_month
    result = more_toothbrushes
    return result

print(solution())