def solution():
    num_figures = 24

    # Calculate the number of figures Angela sold
    num_sold = num_figures / 4

    # Calculate the number of figures remaining after selling
    num_remaining = num_figures - num_sold

    # Calculate the number of figures Angela gave to her daughter
    num_given = num_remaining / 3

    # Calculate the final number of figures Angela has left
    num_left = num_remaining - num_given
    result = num_left
    return result

print(solution())