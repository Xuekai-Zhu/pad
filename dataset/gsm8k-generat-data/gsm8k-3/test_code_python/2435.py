def solution():
    """In 5 years, Frank will be three times as old as Ty is now. Ty is currently 4 years more than two times as old as Carla is now.
    Carla is currently 2 years older than Karen is now.
    If Karen is currently 2 years old, how old will Frank be in 5 years?"""
    # Define Karen's age
    Karen_age = 2

    # Calculate Carla's age
    Carla_age = Karen_age + 2

    # Calculate Ty's age
    Ty_age = 2 * Carla_age + 4

    # Calculate Frank's age in the future
    Frank_age_in_future = 3 * Ty_age

    # Calculate Frank's current age
    Frank_age = Frank_age_in_future - 5

    # Calculate Frank's age in 5 years
    Frank_age_in_5_years = Frank_age + 5

    # Display Frank's age in 5 years
    result = Frank_age_in_5_years
    return result

print(solution())