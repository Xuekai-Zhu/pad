def solution():
    t_shirts = 9
    sweaters = t_shirts * 2
    t_shirts_returned = t_shirts * 3
    sweaters_returned = sweaters / 3
    total_items = t_shirts + sweaters
    total_items_returned = t_shirts_returned + sweaters_returned
    difference = total_items - total_items_returned
    result = difference
    return result

print(solution())