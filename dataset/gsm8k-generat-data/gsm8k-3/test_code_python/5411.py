def solution():
    """A train takes 2 hours longer to go an equal distance of a car. If the car and the train leave station A at the same time, and the car reaches station B 4.5 hours later, calculate the combined time the car and the train take to reach station B."""
    # Let x be the time it takes for the car to reach station B
    # Then, the time it takes for the train to reach station B is x + 2

    # Let d be the distance between station A and B
    # Then, the speed of the car is d/x and the speed of the train is d/(x+2)

    # Since the distance is the same, we can set up the equation:
    # d/x = d/(x+2) + (4.5 - x)/(x+2)
    # Solving for x, we get x = 9

    # Therefore, the time it takes for the car and the train to reach station B is:
    time_total = 9 + 2
    result = time_total
    return result

print(solution())