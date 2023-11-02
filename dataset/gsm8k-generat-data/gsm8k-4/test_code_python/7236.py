def solution():
    """ The school has 14 boys and 10 girls. If 4 boys and 3 girls drop out, how many boys and girls are left? """
    # Define the initial number of boys and girls
    initial_boys = 14
    initial_girls = 10

    # Calculate the number of boys and girls who drop out
    dropped_boys = 4
    dropped_girls = 3

    # Calculate the remaining number of boys and girls
    remaining_boys = initial_boys - dropped_boys
    remaining_girls = initial_girls - dropped_girls

    # return the result
    result = f"There are {remaining_boys} boys and {remaining_girls} girls left."
    return result

print(solution())