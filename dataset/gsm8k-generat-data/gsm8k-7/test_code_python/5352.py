def solution():
    # Let's assume Cooper's age as x
    cooper_age = x
    # Dante's age is twice Cooper's age
    dante_age = 2 * x
    # Maria is one year older than Dante
    maria_age = dante_age + 1
    # The sum of their ages is 31
    total_age = cooper_age + dante_age + maria_age

    # Using the equation above, we can solve for Cooper's age
    x = (31 - 1) / 4
    cooper_age = x
    result = cooper_age
    return result

print(solution())