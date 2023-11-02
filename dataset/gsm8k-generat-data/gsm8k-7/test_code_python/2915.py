def solution():
    adam_age = 8
    tom_age = 12
    combined_age = 44

    # Define the variable for the number of years to solve for
    num_years = 0

    # Use a loop to increment the number of years until the combined age is 44
    while adam_age + tom_age + num_years != combined_age:
        num_years += 1

    result = num_years
    return result

print(solution())