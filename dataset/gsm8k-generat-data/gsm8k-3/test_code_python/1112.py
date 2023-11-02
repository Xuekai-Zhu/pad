def solution():
    """42 raspberries, blackberries, and blueberries were picked in total. If half of all the berries had been raspberries, and a third of the berries were blackberries, how many of them were blueberries?"""
    # Calculate the number of raspberries
    raspberries = 42 / 2

    # Calculate the number of blackberries
    blackberries = 42 / 3

    # Calculate the number of blueberries
    blueberries = 42 - raspberries - blackberries

    # Display the number of blueberries
    result = blueberries
    return result

print(solution())