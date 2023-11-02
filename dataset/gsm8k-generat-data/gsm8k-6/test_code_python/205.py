def solution():
    # Calculate the total number of attendees
    total_attendees = 30 + (30//2)  # half of the guests bring a plus one

    # Calculate the number of plates needed for the 3-course meal
    plates_per_person = 3
    total_plates = total_attendees * plates_per_person

    result = total_plates
    return result

print(solution())