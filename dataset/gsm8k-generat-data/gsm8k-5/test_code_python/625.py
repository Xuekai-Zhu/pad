def solution():
    trash_cans_on_streets = 14  # The council adds 14 trash cans to the streets
    trash_cans_in_stores = trash_cans_on_streets * 2  # Twice as many trash cans are added to the back of stores

    # Calculate the total number of trash cans paid for by the town
    total_trash_cans = trash_cans_on_streets + trash_cans_in_stores
    result = total_trash_cans
    return result

print(solution())