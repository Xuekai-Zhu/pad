def solution():
    # Calculate the total number of planks Andrew used
    bedroom_planks = 8 + 3  # Andrew had to replace 3 planks in his bedroom
    living_room_planks = 20
    kitchen_planks = 11
    guest_bedroom_planks = bedroom_planks - 2  # the guest bedroom took two fewer planks than Andrew's bedroom
    hallway_planks = 2 * 4  # each hallway took four planks
    total_planks_used = bedroom_planks + living_room_planks + kitchen_planks + guest_bedroom_planks + hallway_planks

    # Calculate the number of planks Andrew bought to start with
    initial_planks = total_planks_used + 6  # Andrew had six leftover planks
    result = initial_planks
    return result

print(solution())