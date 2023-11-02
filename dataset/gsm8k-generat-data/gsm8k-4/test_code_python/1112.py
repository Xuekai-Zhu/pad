def solution():
    """42 raspberries, blackberries, and blueberries were picked in total. If half of all the berries had been raspberries, and a third of the berries were blackberries, how many of them were blueberries?"""
    # Define the total number of berries picked
    total = 42

    # Calculate the number of raspberries
    raspberries = total / 2

    # Calculate the number of blackberries
    blackberries = total / 3

    # Calculate the number of blueberries
    blueberries = total - raspberries - blackberries

    result = blueberries
    return result

print(solution())