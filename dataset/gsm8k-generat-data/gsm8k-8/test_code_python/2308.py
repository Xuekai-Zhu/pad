def solution():
    # Define variables for the number of bandages Peggy used and the initial number of bandages in the box
    used_bandages = 2 + 3
    initial_bandages = 2 * 12 - 8

    # Calculate the number of bandages left in the box
    remaining_bandages = initial_bandages - used_bandages
    result = remaining_bandages
    return result

print(solution())