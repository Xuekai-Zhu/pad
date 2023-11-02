def solution():
    space_per_vehicle = 30  # Each vehicle requires 30 spaces
    total_spaces = space_per_vehicle * (3 + 2)  # There are 3 caravans taking up 2 spaces each, in addition to the vehicles that can still park
    spaces_taken = 3 * 2  # There are 3 caravans taking up 2 spaces each
    vehicles_can_park = (total_spaces - spaces_taken) // space_per_vehicle  # Calculate the number of vehicles that can still park

    result = vehicles_can_park
    return result

print(solution())