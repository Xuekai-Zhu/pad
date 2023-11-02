def solution():
    """Jack has been driving for the past 9 years. He drives 37,000 miles every four months. How many miles has Jack driven since he started driving?"""
    # Define the number of years Jack has been driving
    years_driving = 9

    # Define the number of miles Jack drives every four months
    miles_per_interval = 37000

    # Calculate the total number of intervals (four months) Jack has been driving
    total_intervals = years_driving * 3

    # Calculate the total number of miles Jack has driven
    total_miles = total_intervals * miles_per_interval

    # Display the total number of miles Jack has driven
    result = total_miles
    return result

print(solution())