def solution():
    """Mary's sheep can run 12 feet per second, and her sheepdog can run 20 feet per second. A sheep standing 160 feet away from the sheep dog bolts, and the dog runs after it. How many seconds does it take the dog to catch the sheep?"""
    # Define the speeds of the sheep and the sheepdog
    SHEEP_SPEED = 12 # feet per second
    SHEEPDOG_SPEED = 20 # feet per second

    # Define the distance between the sheep and the sheepdog
    DISTANCE = 160 # feet

    # Calculate the time it takes for the sheepdog to catch the sheep
    time = DISTANCE / (SHEEPDOG_SPEED - SHEEP_SPEED)
    
    # Display the time
    result = time
    return result

print(solution())