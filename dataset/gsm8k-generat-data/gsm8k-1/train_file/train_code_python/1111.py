def solution():
    """42 raspberries, blackberries, and blueberries were picked in total. If half of all the berries had been raspberries, and a third of the berries were blackberries, how many of them were blueberries?"""
    total_berries = 42
    raspberries = total_berries / 2
    blackberries = total_berries / 3
    blueberries = total_berries - raspberries - blackberries
    result = blueberries
    return result

print(solution())