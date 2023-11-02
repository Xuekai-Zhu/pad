def solution():
    """Mark is 18 years old. He has a little brother, John, who is 10 years younger. If John and Mark's parents are currently 5 times older than John, how old were they when Mark was born?"""
    mark_age = 18
    john_age = mark_age - 10
    parents_age = 5 * john_age
    parents_age_when_mark_was_born = mark_age + parents_age
    result = parents_age_when_mark_was_born
    return result

print(solution())