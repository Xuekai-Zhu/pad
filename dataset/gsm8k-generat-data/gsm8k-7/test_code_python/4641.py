def solution():
    total_spectators = 10000
    num_men = 7000

    # Calculate the number of women
    num_women = total_spectators - num_men

    # Calculate the number of children
    num_children = 5 * num_women

    result = num_children
    return result

print(solution())