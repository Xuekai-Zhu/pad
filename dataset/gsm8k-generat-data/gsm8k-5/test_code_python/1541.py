def solution():
    initial_bunch_size = 9  # Avery ties 8 bunches of flowers with 9 flowers in each bunch
    new_bunch_size = 12  # Avery wants to put 12 flowers in each bunch

    # Calculate the new number of bunches based on the new bunch size
    new_num_bunches = (8 * initial_bunch_size) // new_bunch_size

    result = new_num_bunches
    return result

print(solution())