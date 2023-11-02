def solution():
    starting_size = 1077 / 6  # Divide the current size by 6 (doubled and then tripled the next year)
    size_last_year = starting_size + 129  # Add the gain from last year to get the starting size of the third year
    fish_per_day = size_last_year * 1.5  # Multiply the starting size by the number of fish each penguin eats per day
    result = fish_per_day
    return result

print(solution())