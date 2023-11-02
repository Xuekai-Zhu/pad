def solution():
    """An organization trying to save endangered species of turtles has taken twice more hawksbill turtles than the number of green turtles into a conservation center. If the number of green turtles is 800, calculate the number of turtles that have been taken into the conservation center."""
    # Define the number of green turtles
    green_turtles = 800

    # Calculate the number of hawksbill turtles as twice more than green turtles
    hawksbill_turtles = 2 * green_turtles

    # Calculate the total number of turtles in the conservation center
    total_turtles = green_turtles + hawksbill_turtles

    # Return the result
    result = total_turtles
    return result

print(solution())