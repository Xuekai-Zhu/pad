def solution():
    # Define the variables
    nina_age = 2 * leonard_age + 4
    jerome_age = 2 * nina_age
    total_age = leonard_age + nina_age + jerome_age

    # Set up the equation to solve for Leonard's age
    leonard_age + nina_age + jerome_age = 36
    leonard_age + (2 * leonard_age + 4) + (2 * (2 * leonard_age + 4)) = 36
    7 * leonard_age = 20
    leonard_age = 20 / 7

    result = leonard_age
    return result

print(solution())