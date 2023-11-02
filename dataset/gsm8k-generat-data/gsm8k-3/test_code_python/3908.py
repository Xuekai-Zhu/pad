def solution():
    """To get clean, Michael takes a bath twice a week and a shower once a week. How many total times does he clean himself in 52 weeks, which is about one year?"""
    # Define the number of times Michael takes a bath and a shower in one week
    baths_per_week = 2
    showers_per_week = 1

    # Calculate the total number of times Michael cleans himself in one year (52 weeks)
    total_cleaning_times = (baths_per_week + showers_per_week) * 52

    # Display the total number of cleaning times
    result = total_cleaning_times
    return result

print(solution())