def solution():
    chocolates_per_weekday = 2
    chocolates_per_weekend = 1
    total_chocolates = 24

    # Calculate the total number of chocolates eaten on weekdays
    chocolates_on_weekdays = chocolates_per_weekday * 5

    # Calculate the total number of chocolates eaten on weekends
    chocolates_on_weekends = chocolates_per_weekend * 2

    # Calculate the total number of weeks it took to finish all the chocolates
    total_weeks = (total_chocolates - chocolates_on_weekends) / chocolates_on_weekdays

    result = total_weeks
    return result

print(solution())