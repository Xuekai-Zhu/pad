def solution():
    """A Lamplighter monkey has long arms and can swing from branch to branch at a speed of 10 feet per second.  But when the monkey is frightened, it will run along the branches at a speed of 15 feet per second.  If a Lamplighter monkey runs for 5 seconds to evade a predator, then swings for another 10 seconds to add distance between itself and the predator, how far, in feet, will the monkey travel?"""
    # Define the speed of the monkey while swinging and running
    SWING_SPEED = 10
    RUN_SPEED = 15

    # Define the time the monkey swings and runs
    SWING_TIME = 10
    RUN_TIME = 5

    # Calculate the distance the monkey travels while swinging and running
    swing_distance = SWING_SPEED * SWING_TIME
    run_distance = RUN_SPEED * RUN_TIME

    # Calculate the total distance the monkey travels
    total_distance = swing_distance + run_distance

    # Display the total distance the monkey traveled
    result = total_distance
    return result

print(solution())