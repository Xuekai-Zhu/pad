def solution():
    """Jack has been driving for the past 9 years. He drives 37,000 miles every four months. How many miles has Jack driven since he started driving?"""
    # Define the number of years Jack has been driving
    years_driven = 9

    # Define the number of miles Jack drives every four months
    miles_per_four_months = 37000

    # Calculate the total number of four-month blocks Jack has been driving
    total_blocks = years_driven * 3

    # Calculate the total number of miles Jack has driven
    total_miles = total_blocks * miles_per_four_months

    # Return the result
    result = total_miles
    return result

print(solution())