def solution():
    boys = 3
    meatballs_per_plate = 3
    meatballs_eaten = 2/3
    meatballs_left = meatballs_per_plate - meatballs_eaten
    total_meatballs_left = boys * meatballs_left
    result = total_meatballs_left
    return result

print(solution())