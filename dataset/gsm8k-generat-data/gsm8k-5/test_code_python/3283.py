def solution():
    total_area = 2300  # The house is 2,300 sq ft total
    common_area = 1000  # The living room, dining room, and kitchen take up 1,000 sq ft
    guest_bedroom = (1/4) * (total_area - common_area)  # The guest bedroom is a quarter of the size of the master bedroom suite
    master_suite = total_area - common_area - guest_bedroom  # The master bedroom suite is the remaining area

    result = master_suite
    return result

print(solution())