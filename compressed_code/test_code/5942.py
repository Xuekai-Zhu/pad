def solution():
    
    num_guests = 30
    num_plus_ones = num_guests // 2
    total_guests = num_guests + num_plus_ones
    num_courses = 3
    plates_per_guest = num_courses
    total_plates = total_guests * plates_per_guest
    result = total_plates
    return result

print(solution())