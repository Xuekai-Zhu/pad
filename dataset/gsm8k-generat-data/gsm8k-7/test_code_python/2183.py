def solution():
    bedroom_planks = 8
    living_room_planks = 20
    kitchen_planks = 11
    guest_bedroom_planks = bedroom_planks - 2
    hallway_planks = 4
    ruined_planks_per_room = 3
    leftover_planks = 6

    # Calculate the total number of planks needed for all rooms including ruined planks
    total_planks = (bedroom_planks + living_room_planks + kitchen_planks + guest_bedroom_planks +
                    (2 * hallway_planks))

    # Subtract the ruined planks from the total
    total_planks -= (ruined_planks_per_room * 2)

    # Add the leftover planks to the total
    total_planks += leftover_planks

    result = total_planks
    return result

print(solution())