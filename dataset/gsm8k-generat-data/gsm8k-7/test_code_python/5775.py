def solution():
    total_spaces = 30
    spaces_per_caravan = 2
    num_caravans = 3

    # Calculate the total number of spaces taken up by the caravans
    total_caravan_spaces = spaces_per_caravan * num_caravans

    # Calculate the total number of spaces left for vehicles to park
    total_spaces_left = total_spaces - total_caravan_spaces

    # Calculate the number of vehicles that can still park
    num_vehicles_left = total_spaces_left // 1
    result = num_vehicles_left
    return result

print(solution())