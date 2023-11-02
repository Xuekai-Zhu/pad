def solution():
    """To get clean, Michael takes a bath twice a week and a shower once a week. How many total times does he clean himself in 52 weeks, which is about one year?"""
    # Define the number of times Michael takes a bath and shower per week
    baths_per_week = 2
    showers_per_week = 1

    # Calculate the total number of times Michael cleans himself in one week
    total_cleaning_per_week = baths_per_week + showers_per_week

    # Calculate the total number of times Michael cleans himself in 52 weeks
    total_cleaning_per_year = total_cleaning_per_week * 52

    # return the result
    result = total_cleaning_per_year
    return result

print(solution())