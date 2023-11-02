def solution():
    # Calculate the number of cups of tea that Marco can make from a box of tea leaves
    cups_per_box = 28 / (1/5)  # a fifth of an ounce of tea leaves is used for each cup of tea
    # Calculate the number of weeks that Marco can make tea from a box of tea leaves based on daily use
    weeks_per_box = cups_per_box / 7
    result = weeks_per_box
    return result

print(solution())