def solution():
    """Omi is twice as old as Kimiko. Arlette is 3/4 times as old as Kimiko. If Kimiko is 28 years old, calculate the average age of the three?"""
    # Calculate Omi's age
    omi_age = 2 * 28

    # Calculate Arlette's age
    arlette_age = (3/4) * 28

    # Calculate the total age of the three
    total_age = kimiko_age + omi_age + arlette_age

    # Calculate the average age of the three
    average_age = total_age / 3

    # Display the average age
    result = average_age
    return result

print(solution())