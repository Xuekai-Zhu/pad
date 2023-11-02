def solution():
    mice_per_week = 1 / 4  # The snake eats one mouse every 4 weeks
    weeks_in_decade = 10 * 52  # There are 52 weeks in a year, and the decade has 10 years

    # Calculate the total number of mice the snake will eat in a decade
    total_mice = mice_per_week * weeks_in_decade

    result = total_mice
    return result

print(solution())