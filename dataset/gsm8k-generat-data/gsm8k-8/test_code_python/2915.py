def solution():
    # Define the current ages of Adam and Tom
    adam_age = 8
    tom_age = 12

    # Define the target age for their combined age
    target_age = 44

    # Set the number of years to 0
    num_years = 0

    # Loop until their combined age is equal to the target age
    while adam_age + tom_age != target_age:
        # Increment the number of years
        num_years += 1

        # Increase the ages of both brothers by 1
        adam_age += 1
        tom_age += 1

    result = num_years
    return result

print(solution())