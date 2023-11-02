def solution():
    """Mark is 18 years old. He has a little brother, John, who is 10 years younger. If John and Mark's parents are currently 5 times older than John, how old were they when Mark was born?"""
    # Define Mark's age
    mark_age = 18

    # Define John's age
    john_age = mark_age - 10

    # Calculate the current age of John and Mark's parents
    parents_age = john_age * 5

    # Calculate the age of John and Mark's parents when Mark was born
    parents_age_when_mark_born = parents_age - mark_age

    # return the result
    result = parents_age_when_mark_born
    return result

print(solution())