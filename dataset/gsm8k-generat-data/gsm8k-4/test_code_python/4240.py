def solution():
    """When Diane turns 30, she will be half the age of Alex and twice as old as Allison. Diane is 16 years old now. What is the sum of the ages of Alex and Allison now?"""
    # Define Diane's current age
    diane_age = 16

    # Define the age difference between Diane and Alex
    alex_age_difference = 30 - diane_age - 15

    # Calculate Alex's current age
    alex_age = diane_age + alex_age_difference

    # Calculate Allison's current age
    allison_age = diane_age / 2

    # Calculate the sum of Alex and Allison's current ages
    sum_of_ages = alex_age + allison_age

    result = sum_of_ages
    return result

print(solution())