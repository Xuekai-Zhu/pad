def solution():
    
    length = 600
    width = 400
    perimeter = 2 * (length + width)
    times_patrolled = 10 - 2
    total_distance = perimeter * times_patrolled
    result = total_distance
    return result

print(solution())