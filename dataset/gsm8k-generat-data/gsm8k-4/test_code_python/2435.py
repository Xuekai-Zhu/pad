def solution():
    """In 5 years, Frank will be three times as old as Ty is now. Ty is currently 4 years more than two times as old as Carla is now. Carla is currently 2 years older than Karen is now. If Karen is currently 2 years old, how old will Frank be in 5 years?"""
    # Define Karen's age
    karen_age = 2

    # Calculate Carla's age
    carla_age = karen_age + 2

    # Calculate Ty's age
    ty_age = 2 * carla_age + 4

    # Calculate Frank's age in 5 years
    frank_age_in_5_years = 3 * ty_age - 5

    # return the result
    result = frank_age_in_5_years
    return result

print(solution())