def solution():
    building_count = 4
    studio_count = 10
    two_person_count = 20
    four_person_count = 5
    max_occupancy = (studio_count * 1) + (two_person_count * 2) + (four_person_count * 4)
    max_occupancy = max_occupancy * building_count
    current_occupancy = max_occupancy * .75
    result = current_occupancy
    
    return result

print(solution())