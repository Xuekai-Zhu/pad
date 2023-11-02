def solution():
    total_potatoes = 67
    wedge_potatoes = 13

    remaining_potatoes = total_potatoes - wedge_potatoes
    chips_potatoes = remaining_potatoes / 2
    fries_potatoes = remaining_potatoes / 2

    # Calculate the number of wedges from the cut potatoes
    num_wedges = wedge_potatoes * 8

    # Calculate the number of chips from the remaining potatoes
    num_chips = chips_potatoes * 20

    # Calculate the difference between the number of chips and wedges
    difference = num_chips - num_wedges
    result = difference
    return result

print(solution())