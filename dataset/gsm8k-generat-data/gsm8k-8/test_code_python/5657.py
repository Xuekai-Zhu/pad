def solution():
    # Define the number of weeks in a decade
    weeks_in_decade = 52 * 10

    # Calculate the number of mice the snake will eat in a decade
    mice_per_week = 1
    mice_per_decade = int(weeks_in_decade / 4) * mice_per_week

    result = mice_per_decade
    return result

print(solution())