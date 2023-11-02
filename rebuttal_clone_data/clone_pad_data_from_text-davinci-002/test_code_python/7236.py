def solution():
    boys = 14
    girls = 10
    boys_dropped = 4
    girls_dropped = 3
    boys_left = boys - boys_dropped
    girls_left = girls - girls_dropped
    result = boys_left, girls_left
    return result

print(solution())