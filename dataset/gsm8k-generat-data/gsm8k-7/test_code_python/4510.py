def solution():
    mark_age = 18
    john_age = mark_age - 10
    parent_age = 5 * john_age

    # Calculate the age difference between Mark and his parents
    parent_mark_age_diff = mark_age - parent_age

    # Calculate the age of Mark's parents when he was born
    parent_age_at_birth = mark_age - parent_mark_age_diff
    result = parent_age_at_birth
    return result

print(solution())