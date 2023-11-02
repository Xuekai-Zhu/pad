def solution():
    doughnuts_per_dozen = 12  # There are 12 doughnuts in a dozen
    doughnuts_per_box = 2 * doughnuts_per_dozen  # There are 2 dozens in a box
    doughnuts_eaten = 8  # The family ate 8 doughnuts

    # Calculate the number of doughnuts left in the box
    doughnuts_left = doughnuts_per_box - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())