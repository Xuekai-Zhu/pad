def solution():
    
    total_balls = 15 + 5
    baskets = 5
    removed_by_3 = 8
    removed_by_2 = (total_balls * baskets - 3 * removed_by_3 - 56) / 2
    result = removed_by_2
    return result

print(solution())