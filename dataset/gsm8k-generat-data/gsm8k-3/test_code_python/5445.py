def solution():
    """Kennedy’s car can drive 19 miles per gallon of gas. She was able to drive 15 miles to school, 6 miles to the softball park, 2 miles to a burger restaurant, 4 miles to her friend’s house, and 11 miles home before she ran out of gas. How many gallons of gas did she start with?"""
    # Define Kennedy's car's mileage per gallon
    MILEAGE = 19

    # Define the distances traveled
    distances = [15, 6, 2, 4, 11]

    # Calculate the total distance traveled
    total_distance = sum(distances)

    # Calculate the number of gallons of gas used
    gallons_used = total_distance / MILEAGE

    # Calculate the number of gallons of gas Kennedy started with
    gallons_started_with = gallons_used + 1

    # Display the number of gallons Kennedy started with
    result = gallons_started_with
    return result

print(solution())