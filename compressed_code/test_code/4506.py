def solution():
    
    starting_steaks = 25
    remaining_steaks = 12
    sold_steaks = starting_steaks - remaining_steaks
    additional_sold_steaks = 4
    total_sold_steaks = sold_steaks + additional_sold_steaks
    result = total_sold_steaks
    return result

print(solution())