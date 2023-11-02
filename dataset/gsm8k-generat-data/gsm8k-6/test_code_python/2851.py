def solution():
    # Assigning values to variables
    Aaron_age = 15
    Henry_sister_age = 3 * Aaron_age
    Henry_age = 4 * Henry_sister_age

    # Finding the combined age of the siblings
    combined_age = Aaron_age + Henry_sister_age + Henry_age
    result = combined_age
    return result

print(solution())