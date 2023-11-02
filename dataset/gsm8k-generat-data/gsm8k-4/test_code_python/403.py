def solution():
    """Omi is twice as old as Kimiko. Arlette is 3/4 times as old as Kimiko. If Kimiko is 28 years old, calculate the average age of the three?"""
    # Define Kimiko's age
    kimiko_age = 28

    # Calculate Omi's age
    omi_age = kimiko_age * 2

    # Calculate Arlette's age
    arlette_age = kimiko_age * 3/4

    # Calculate the average age of the three
    average_age = (kimiko_age + omi_age + arlette_age) / 3
    
    result = round(average_age, 2)
    return result

print(solution())