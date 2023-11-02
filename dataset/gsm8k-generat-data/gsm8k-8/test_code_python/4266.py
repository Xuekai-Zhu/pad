def solution():
    # Calculate the initial number of chocolate bars each person received
    initial_distribution = 20 / 5

    # Calculate the number of chocolate bars each person gave to their father
    given_to_father = initial_distribution / 2

    # Calculate the number of chocolate bars Matilda's father had after receiving from his children and giving to his wife and himself
    father_chocolates = ((4 * given_to_father) - 2) - 3

    result = father_chocolates
    return result

print(solution())