def solution():
    """The sum of the ages of three boys is 29. If two of the boys are the same age and the third boy is 11 years old, how old are the other two boys?"""
    # Define the variables
    age_1 = 0
    age_2 = 0
    age_3 = 11
    total_age = 29

    # Solve for the ages of the two boys
    for age in range(1, total_age):
        if age * 2 + age_3 == total_age:
            age_1 = age
            age_2 = age
            break

    # Display the ages of the two boys
    result = (age_1, age_2)
    return result

print(solution())