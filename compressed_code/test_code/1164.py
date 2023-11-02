def solution():
    
    total_brownies = 24
    eaten_by_tina = 2 * 5
    eaten_by_husband = 5
    shared_with_guests = 4
    total_eaten = eaten_by_tina + eaten_by_husband + shared_with_guests
    brownies_left = total_brownies - total_eaten
    result = brownies_left
    return result

print(solution())