def solution():
    # Define the variables
    cooper_age = 0
    dante_age = 0
    maria_age = 0

    # Set up the equations
    dante_age = 2 * cooper_age
    maria_age = dante_age + 1
    total_age = cooper_age + dante_age + maria_age

    # Solve for cooper_age
    cooper_age = (total_age - 1) / 4
    result = cooper_age
    return result

print(solution())