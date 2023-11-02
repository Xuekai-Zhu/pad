def solution():
    total_age = 29
    boy_age = 11

    # Calculate the age of the two boys who are the same age
    same_age = (total_age - boy_age) / 2

    # Return the age of both boys as a tuple
    result = (same_age, same_age)
    return result

print(solution())