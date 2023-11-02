def solution():
    
    total_candy_collected = 68
    candy_eaten_by_each = 4
    total_candy_eaten = candy_eaten_by_each * 2
    candy_left = total_candy_collected - total_candy_eaten
    result = candy_left
    return result

print(solution())