def solution():
    nathan_hours_per_day = 3
    nathan_days_per_week = 7
    nathan_weeks_played = 2

    tobias_hours_per_day = 5
    tobias_days_per_week = 7
    tobias_weeks_played = 1

    # Calculate the total number of hours Nathan played
    nathan_total_hours = nathan_hours_per_day * nathan_days_per_week * nathan_weeks_played

    # Calculate the total number of hours Tobias played
    tobias_total_hours = tobias_hours_per_day * tobias_days_per_week * tobias_weeks_played

    # Calculate the total number of hours they played in total
    total_hours = nathan_total_hours + tobias_total_hours
    result = total_hours
    return result

print(solution())