def solution():
    initial_bones = 4  # Juniper starts with 4 bones
    doubled_bones = initial_bones * 2  # Juniper's master gives her enough bones to double her number of bones
    stolen_bones = 2  # The neighbor's dog steals two of Juniper's bones

    # Calculate the number of bones Juniper has remaining
    remaining_bones = doubled_bones - stolen_bones
    result = remaining_bones
    return result

print(solution())