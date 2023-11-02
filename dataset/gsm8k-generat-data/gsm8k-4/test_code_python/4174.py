def solution():
    """Ronnie is a train engineer. His train pulls 3 red boxcars, 4 blue boxcars, and 7 black boxcars. If the black boxcars can each hold 4000 pounds of coal, which is half as much as what the blue boxcars can hold, and the red boxcars can hold 3 times as much as the blue boxcars, how many pounds of coal can all of the train's boxcars combined hold?"""
    # Define the capacity of a black boxcar in pounds
    black_capacity = 4000

    # Calculate the capacity of a blue boxcar in pounds
    blue_capacity = black_capacity * 2

    # Calculate the capacity of a red boxcar in pounds
    red_capacity = blue_capacity * 3

    # Calculate the total capacity of all the boxcars in pounds
    total_capacity = (red_capacity * 3) + (blue_capacity * 4) + (black_capacity * 7)

    result = total_capacity
    return result

print(solution())