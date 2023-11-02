def solution():
    """During a staff meeting, 50 doughnuts were served. If each of the 19 staff ate 2 doughnuts, how many doughnuts are left?"""
    total_doughnuts = 50
    staff_members = 19
    doughnuts_eaten = staff_members * 2
    doughnuts_left = total_doughnuts - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())