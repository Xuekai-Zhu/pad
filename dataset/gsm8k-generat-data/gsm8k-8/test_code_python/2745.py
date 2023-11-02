def solution():
    total_doughnuts = 50
    staff_members = 19
    doughnuts_per_staff = 2

    doughnuts_eaten = staff_members * doughnuts_per_staff
    doughnuts_left = total_doughnuts - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())