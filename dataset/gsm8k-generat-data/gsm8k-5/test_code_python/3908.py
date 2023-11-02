def solution():
    # Calculate the total number of times Michael cleans himself in a week
    clean_per_week = 2 + 1  # Michael takes 2 baths and 1 shower per week

    # Calculate the total number of times Michael cleans himself in a year
    clean_per_year = clean_per_week * 52  # There are 52 weeks in a year

    result = clean_per_year
    return result

print(solution())