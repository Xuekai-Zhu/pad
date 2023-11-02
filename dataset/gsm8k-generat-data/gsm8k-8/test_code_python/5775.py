def solution():
    total_spaces = 30
    caravan_spaces = 2
    occupied_spaces = caravan_spaces * 3

    remaining_spaces = total_spaces - occupied_spaces
    vehicles_can_park = remaining_spaces // caravan_spaces
    result = vehicles_can_park
    return result

print(solution())