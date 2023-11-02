def solution():
    
    bottom_half_rows = 5
    top_half_rows = 5
    bottom_half_bricks = 12
    top_half_bricks = 8
    total_bricks = (bottom_half_rows * bottom_half_bricks) + (top_half_rows * top_half_bricks)
    result = total_bricks
    return result

print(solution())