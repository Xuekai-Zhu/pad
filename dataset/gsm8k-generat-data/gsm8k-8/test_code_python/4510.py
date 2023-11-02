def solution():
    # Calculate John's age
    john_age = 18 - 10

    # Calculate the parents' current age
    parent_age = john_age * 5

    # Calculate the age difference between Mark and his parents
    age_difference = parent_age - 18

    # Calculate the parents' age when Mark was born
    parents_age_when_mark_was_born = age_difference + 18

    result = parents_age_when_mark_was_born
    return result

print(solution())