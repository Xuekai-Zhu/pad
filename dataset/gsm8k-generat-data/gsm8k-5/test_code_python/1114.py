def solution():
    donuts_per_day = 10
    days = 12
    total_donuts_made = donuts_per_day * days
    donuts_eaten_by_jeff = 12
    donuts_eaten_by_chris = 8
    remaining_donuts = total_donuts_made - donuts_eaten_by_jeff - donuts_eaten_by_chris
    donuts_per_box = 10
    boxes_filled = remaining_donuts // donuts_per_box
    result = boxes_filled
    return result

print(solution())