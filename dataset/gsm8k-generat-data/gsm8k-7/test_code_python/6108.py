def solution():
    num_rooms_grant = 2
    ratio_heidi = 3
    ratio_grant = 1 / 9

    # Calculate the total number of rooms in Heidi's apartment
    num_rooms_heidi = num_rooms_grant / ratio_grant * ratio_heidi

    # Calculate the total number of rooms in Danielle's apartment (which has 1/3 as many rooms as Heidi's apartment)
    num_rooms_danielle = num_rooms_heidi / 3
    result = num_rooms_danielle
    return result

print(solution())