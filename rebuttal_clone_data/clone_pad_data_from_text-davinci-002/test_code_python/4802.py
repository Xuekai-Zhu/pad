def solution():
    minutes_per_charge = 10
    minutes_per_room = 4
    num_rooms = 3 + 1 + 1
    num_charges = num_rooms / minutes_per_charge
    result = num_charges
    return result

print(solution())