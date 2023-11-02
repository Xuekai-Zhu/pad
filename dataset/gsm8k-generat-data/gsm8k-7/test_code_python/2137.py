def solution():
    initial_tomatoes = 36
    growth_factor = 100

    # Calculate the total number of tomatoes after vacation
    total_tomatoes = initial_tomatoes * growth_factor

    # Calculate the number of tomatoes that grew in his absence
    grew_tomatoes = total_tomatoes - initial_tomatoes
    result = grew_tomatoes
    return result

print(solution())