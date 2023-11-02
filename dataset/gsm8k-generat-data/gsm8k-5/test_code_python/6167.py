def solution():
    total_potatoes = 67  # Cynthia harvested 67 potatoes
    wedges = 13  # Cynthia cut 13 potatoes into wedges
    remaining_potatoes = total_potatoes - wedges  # Cynthia has the remaining potatoes
    half_remaining_potatoes = remaining_potatoes / 2  # Cynthia halved the remaining potatoes

    # Calculate the number of potato chips Cynthia made
    potato_chips = half_remaining_potatoes * 20  # 1 potato makes 20 potato chips

    # Calculate the number of wedges Cynthia made
    num_wedges = wedges * 8  # 1 potato can be cut into 8 wedges

    # Calculate the difference between the number of potato chips and wedges
    difference = potato_chips - num_wedges
    result = difference
    return result

print(solution())