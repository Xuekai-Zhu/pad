def solution():
    # Let's first find the current age difference between James and John
    age_difference = 35 - 23

    # If James is X years old now, then John is X + age_difference years old
    # Tim is 5 less than twice John's age, so we can write an equation as follows:
    # 79 = 2*(X + age_difference) - 5
    # Solving for X gives us James's current age
    james_age = (79 + 5) / 2 - age_difference
    result = james_age
    return result

print(solution())