def solution():
    total_brownies = 24
    eaten_by_Tina = 2 * 5
    eaten_by_husband = 1 * 5
    shared_with_guests = 4
    left_over_brownies = total_brownies - eaten_by_Tina - eaten_by_husband - shared_with_guests
    result = left_over_brownies
    return result

print(solution())