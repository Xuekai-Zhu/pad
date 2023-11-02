def solution():
    num_days_per_week = 7
    num_people_two_plate_days = 4
    num_people_one_plate_days = 2
    num_plates_per_person_one_plate_days = 1
    num_plates_per_person_two_plate_days = 2

    # Calculate the total number of plates needed for the two-plate days
    total_plates_two_plate_days = num_people_two_plate_days * num_plates_per_person_two_plate_days * (num_days_per_week - num_people_one_plate_days)

    # Calculate the total number of plates needed for the one-plate days
    total_plates_one_plate_days = num_people_one_plate_days * num_plates_per_person_one_plate_days * num_days_per_week

    # Calculate the total number of plates needed
    total_plates_needed = total_plates_two_plate_days + total_plates_one_plate_days
    result = total_plates_needed
    return result

print(solution())