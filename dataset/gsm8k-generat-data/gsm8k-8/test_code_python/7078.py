def solution():
    # Calculate the bread eaten by the first duck
    first_duck_eaten = 30 / 2

    # Calculate the total bread eaten by all ducks
    total_eaten = first_duck_eaten + 13 + 7

    # Calculate the total bread thrown in the pond
    total_thrown = total_eaten + 30
    result = total_thrown
    return result

print(solution())