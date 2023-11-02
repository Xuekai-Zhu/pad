def solution():
    spaces_for_vehicle = 30
    spaces_for_caravan = 2
    number_of_caravans = 3
    total_spaces_used = number_of_caravans * spaces_for_caravan
    remaining_spaces = spaces_for_vehicle - total_spaces_used
    result = remaining_spaces / spaces_for_vehicle
    return result

print(solution())