def solution():
    num_guests = 30
    num_plus_ones = num_guests / 2 # half of guests bring a plus one
    total_people = num_guests + num_plus_ones # total number of people at the party

    num_courses = 3
    num_plates = num_courses * total_people # number of plates needed for all guests

    result = num_plates
    return result

print(solution())