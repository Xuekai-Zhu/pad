def solution():
    """A soccer ball takes twenty minutes to inflate. Alexia and Ermias are inflating
    balls, with Alexia inflating 20 balls and Ermias inflating 5 more balls than Alexia.
    Calculate the total time in minutes they took to inflate all the soccer balls."""
    # Define the time it takes to inflate one ball in minutes
    INFLATION_TIME = 20

    # Define the number of balls each person is inflating
    alexia_balls = 20
    ermias_balls = alexia_balls + 5

    # Calculate the total number of balls being inflated
    total_balls = alexia_balls + ermias_balls

    # Calculate the total time to inflate all the balls
    total_time = total_balls * INFLATION_TIME

    # Display the total time
    result = total_time
    return result

print(solution())