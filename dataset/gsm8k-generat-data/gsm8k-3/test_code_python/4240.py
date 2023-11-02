def solution():
    """When Diane turns 30, she will be half the age of Alex and twice as old as Allison. Diane is 16 years old now. What is the sum of the ages of Alex and Allison now?"""
    # Define Diane's current age
    diane_age = 16

    # Calculate Alex's age when Diane turns 30
    alex_age = (30 - diane_age) * 2

    # Calculate Allison's age when Diane turns 30
    allison_age = (30 - diane_age) / 2

    # Calculate the sum of Alex and Allison's current ages
    total_age = alex_age + allison_age

    # Display the sum of their ages
    result = total_age
    return result

print(solution())