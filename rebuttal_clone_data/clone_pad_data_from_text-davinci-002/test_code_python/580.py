def solution():
    rows = 10
    bottom_rows = rows / 2
    top_rows = rows - bottom_rows
    bottom_bricks = 12
    top_bricks = 8
    total_bricks = (bottom_rows * bottom_bricks) + (top_rows * top_bricks)
    result = total_bricks
    return result

print(solution())