def solution():
    # Calculate the total number of trash cans paid for by the council
    trash_cans_front = 14  # number of trash cans added to the streets
    trash_cans_back = 2 * trash_cans_front  # twice as many trash cans added to the back of stores
    total_trash_cans = trash_cans_front + trash_cans_back  # total number of trash cans paid for
    result = total_trash_cans
    return result

print(solution())