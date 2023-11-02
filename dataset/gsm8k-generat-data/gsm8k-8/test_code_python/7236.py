def solution():
    # Define the initial number of boys and girls
    initial_boys = 14
    initial_girls = 10

    # Subtract the number of boys and girls who drop out
    remaining_boys = initial_boys - 4
    remaining_girls = initial_girls - 3

    result = (remaining_boys, remaining_girls)
    return result

print(solution())