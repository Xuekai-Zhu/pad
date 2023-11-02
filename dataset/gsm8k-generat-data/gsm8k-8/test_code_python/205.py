def solution():
    # Calculate the total number of guests including plus ones
    total_guests = 30 + (30/2)

    # Calculate the number of plates needed per course
    plates_per_course = total_guests * 3

    # Calculate the total number of plates needed
    total_plates = plates_per_course
    result = total_plates
    return result

print(solution())