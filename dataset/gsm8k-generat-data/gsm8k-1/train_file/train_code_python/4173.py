def solution():
    """Ronnie is a train engineer. His train pulls 3 red boxcars, 4 blue boxcars, and 7 black boxcars. If the black boxcars can each hold 4000 pounds of coal, which is half as much as what the blue boxcars can hold, and the red boxcars can hold 3 times as much as the blue boxcars, how many pounds of coal can all of the train's boxcars combined hold?"""
    black_capacity = 4000
    blue_capacity = black_capacity * 2
    red_capacity = blue_capacity * 3
    total_capacity = (3 * red_capacity) + (4 * blue_capacity) + (7 * black_capacity)
    result = total_capacity
    return result

print(solution())