def solution():
    """The sum of Mario and Maria's ages now is 7. Mario is 1 year older than Maria. How old is Mario?"""
    # Define the sum of Mario and Maria's ages
    total_age = 7

    # Define the age difference between Mario and Maria
    age_difference = 1

    # Calculate Maria's age
    maria_age = (total_age - age_difference) / 2

    # Calculate Mario's age
    mario_age = maria_age + age_difference

    result = mario_age
    return result

print(solution())