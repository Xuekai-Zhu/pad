def solution():
    num_rooms = 13
    num_rooms_with_2_beds = 8
    num_rooms_with_3_beds = num_rooms - num_rooms_with_2_beds

    # Calculate the total number of beds in rooms with 2 beds
    total_beds_in_2_bed_rooms = num_rooms_with_2_beds * 2

    # Calculate the total number of beds in rooms with 3 beds
    total_beds_in_3_bed_rooms = num_rooms_with_3_beds * 3

    # Calculate the total number of beds in all rooms
    total_beds = total_beds_in_2_bed_rooms + total_beds_in_3_bed_rooms
    result = total_beds
    return result

print(solution())