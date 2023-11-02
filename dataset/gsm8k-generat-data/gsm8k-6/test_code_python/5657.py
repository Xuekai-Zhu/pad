def solution():
    # Calculate the total number of mice eaten by Gina's snake in a decade (10 years)
    mice_per_year = 52/4  # since there are 52 weeks in a year and the snake eats one mouse every 4 weeks
    mice_in_decade = mice_per_year * 10
    result = mice_in_decade
    return result

print(solution())