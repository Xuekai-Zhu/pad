def solution():
    num_rooms_with_2_beds = 8
    num_rooms_with_3_beds = 13 - num_rooms_with_2_beds
    total_beds = 2 * num_rooms_with_2_beds + 3 * num_rooms_with_3_beds
    result = total_beds
    return result

print(solution())