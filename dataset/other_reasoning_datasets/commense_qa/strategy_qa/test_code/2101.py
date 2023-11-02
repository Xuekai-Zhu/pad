def solution():
    number_of_people_in_obama_family = 4 # 1 husband, 1 wife, 2 children
    max_seating_capacity_of_jaguar = 2
    if number_of_people_in_obama_family <= max_seating_capacity_of_jaguar:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())