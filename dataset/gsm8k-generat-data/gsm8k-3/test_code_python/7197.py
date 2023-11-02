def solution():
    """An organization trying to save endangered species of turtles has taken twice more hawksbill turtles than the number of green turtles into a conservation center. If the number of green turtles is 800, calculate the number of turtles that have been taken into the conservation center."""
    # Define the number of green turtles
    green_turtles = 800

    # Calculate the number of hawksbill turtles
    hawksbill_turtles = 2 * green_turtles + green_turtles * 2

    # Calculate the total number of turtles taken into the conservation center
    total_turtles = green_turtles + hawksbill_turtles

    # Display the total number of turtles taken into the conservation center
    result = total_turtles
    return result

print(solution())