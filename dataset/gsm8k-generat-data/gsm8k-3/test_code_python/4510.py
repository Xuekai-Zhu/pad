def solution():
    """Mark is 18 years old. He has a little brother, John, who is 10 years younger. If John and Mark's parents are currently 5 times older than John, how old were they when Mark was born?"""
    # Define Mark's age and John's age
    mark_age = 18
    john_age = mark_age - 10

    # Define the ratio of parent's age to John's age
    parent_john_ratio = 5

    # Calculate the current age of John's parents
    parent_age = john_age * parent_john_ratio

    # Calculate the age gap between Mark and John's parents
    age_gap = mark_age - john_age

    # Calculate the age of Mark's parents when he was born
    parent_age_at_birth = parent_age - age_gap

    # Display the parents' age when Mark was born
    result = parent_age_at_birth
    return result

print(solution())