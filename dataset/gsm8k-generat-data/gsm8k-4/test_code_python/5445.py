def solution():
    """Kennedy’s car can drive 19 miles per gallon of gas. She was able to drive 15 miles to school, 6 miles to the softball park, 2 miles to a burger restaurant, 4 miles to her friend’s house, and 11 miles home before she ran out of gas. How many gallons of gas did she start with?"""
    # Define the total distance traveled
    total_distance = 15 + 6 + 2 + 4 + 11

    # Define the miles per gallon
    miles_per_gallon = 19

    # Calculate the number of gallons used
    gallons_used = total_distance / miles_per_gallon

    # Calculate the number of gallons Kennedy started with
    gallons_started_with = gallons_used + 1

    result = gallons_started_with
    return result

print(solution())