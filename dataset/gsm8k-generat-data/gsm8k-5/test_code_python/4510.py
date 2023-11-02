def solution():
    john_age = 18 - 10  # John is currently 10 years younger than Mark
    parents_age = 5 * john_age  # The parents are currently 5 times older than John
    mark_birth_year = 18  # Mark is currently 18 years old

    # Calculate the parents' age when Mark was born
    parents_age_at_birth = parents_age - mark_birth_year
    result = parents_age_at_birth
    return result

print(solution())