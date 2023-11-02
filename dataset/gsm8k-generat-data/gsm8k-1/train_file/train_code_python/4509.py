def solution():
    """Mark is 18 years old. He has a little brother, John, who is 10 years younger. If John and Mark's parents are currently 5 times older than John, how old were they when Mark was born?"""
    mark_age = 18
    john_age = mark_age - 10
    parent_age = john_age * 5
    age_difference = mark_age + john_age
    parent_age_when_mark_was_born = parent_age - age_difference
    result = parent_age_when_mark_was_born
    return result

print(solution())