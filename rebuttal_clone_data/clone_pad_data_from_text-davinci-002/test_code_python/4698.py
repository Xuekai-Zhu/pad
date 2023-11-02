def solution():
    masks_per_package = 100
    number_of_people = 4
    days_per_mask = 4
    total_days = masks_per_package * days_per_mask / number_of_people
    result = total_days
    return result

print(solution())