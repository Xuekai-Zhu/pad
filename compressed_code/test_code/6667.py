def solution():
    
    type_a_bricks = 40
    type_b_bricks = type_a_bricks / 2
    total_bricks = 150
    other_bricks = total_bricks - (type_a_bricks + type_b_bricks)
    result = other_bricks
    return result

print(solution())