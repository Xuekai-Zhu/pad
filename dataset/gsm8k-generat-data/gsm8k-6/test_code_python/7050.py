def solution():
    # Calculate the total number of bricks used
    total_bricks = 6 * 10 * 4  # 6 courses per wall, 10 bricks per course, 4 walls in total
    total_bricks -= 2 * 10  # two courses of the last wall were not finished
    result = total_bricks
    return result

print(solution())