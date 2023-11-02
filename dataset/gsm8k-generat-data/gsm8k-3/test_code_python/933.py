def solution():
    """John climbs 3 staircases.  The first staircase has 20 steps.  The next has twice as many steps as the first.  
    The final staircase has 10 fewer steps than the second one.  Each step is 0.5 feet.  How many feet did he climb?"""
    # Define the number of steps in each staircase
    steps1 = 20
    steps2 = steps1 * 2
    steps3 = steps2 - 10

    # Calculate the total number of steps climbed
    total_steps = steps1 + steps2 + steps3

    # Calculate the total distance climbed in feet
    feet_per_step = 0.5
    total_distance = total_steps * feet_per_step

    # Display the total distance climbed
    result = total_distance
    return result

print(solution())