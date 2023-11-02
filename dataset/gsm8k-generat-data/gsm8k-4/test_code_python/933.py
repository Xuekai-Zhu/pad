def solution():
    """John climbs 3 staircases. The first staircase has 20 steps. The next has twice as many steps as the first. The final staircase has 10 fewer steps than the second one. Each step is 0.5 feet. How many feet did he climb?"""
    # Define the number of steps in each staircase
    steps1 = 20
    steps2 = 2 * steps1
    steps3 = steps2 - 10

    # Define the distance climbed for each staircase
    distance1 = steps1 * 0.5
    distance2 = steps2 * 0.5
    distance3 = steps3 * 0.5

    # Calculate the total distance climbed
    total_distance = distance1 + distance2 + distance3

    # return the result
    result = total_distance
    return result

print(solution())