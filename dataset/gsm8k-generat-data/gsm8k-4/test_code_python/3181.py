def solution():
    """Mary's sheep can run 12 feet per second, and her sheepdog can run 20 feet per second. A sheep standing 160 feet away from the sheep dog bolts, and the dog runs after it. How many seconds does it take the dog to catch the sheep?"""
    # Define the speeds of the sheep and the sheepdog
    sheep_speed = 12
    sheepdog_speed = 20

    # Define the distance between the sheep and the sheepdog
    distance = 160

    # Calculate the time it takes for the sheepdog to catch up to the sheep
    time = distance / (sheepdog_speed - sheep_speed)

    # Return the result rounded to 2 decimal places
    result = round(time, 2)
    return result

print(solution())