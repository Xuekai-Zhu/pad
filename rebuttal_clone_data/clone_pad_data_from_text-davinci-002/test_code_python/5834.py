def solution():
    front_parking_spaces = 52
    back_parking_spaces = 38
    cars_parked = 39
    back_parking_spaces_filled = back_parking_spaces / 2
    parking_spaces_still_available = front_parking_spaces + back_parking_spaces - (cars_parked + back_parking_spaces_filled)
    result = parking_spaces_still_available

    return result

print(solution())