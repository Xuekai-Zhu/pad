def solution():
    """The school has 14 boys and 10 girls. If 4 boys and 3 girls drop out, how many boys and girls are left?"""
    # Define the initial number of boys and girls
    initial_boys = 14
    initial_girls = 10

    # Define the number of boys and girls that drop out
    dropouts_boys = 4
    dropouts_girls = 3

    # Calculate the remaining number of boys and girls
    remaining_boys = initial_boys - dropouts_boys
    remaining_girls = initial_girls - dropouts_girls

    # Display the remaining number of boys and girls
    result = (remaining_boys, remaining_girls)
    return result

print(solution())