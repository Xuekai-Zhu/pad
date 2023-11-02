def solution():
    """Ronnie is a train engineer.  His train pulls 3 red boxcars, 4 blue boxcars, and 7 black boxcars.  If the black boxcars can each hold 4000 pounds of coal, which is half as much as what the blue boxcars can hold, and the red boxcars can hold 3 times as much as the blue boxcars, how many pounds of coal can all of the train's boxcars combined hold?"""
    # Define the coal capacity of a black boxcar
    BLACK_CAPACITY = 4000

    # Define the coal capacity of a blue boxcar
    BLUE_CAPACITY = BLACK_CAPACITY * 2

    # Define the coal capacity of a red boxcar
    RED_CAPACITY = BLUE_CAPACITY * 3

    # Calculate the total coal capacity of the train's boxcars
    total_capacity = (3 * RED_CAPACITY) + (4 * BLUE_CAPACITY) + (7 * BLACK_CAPACITY)

    # Display the total coal capacity
    result = total_capacity
    return result

print(solution())