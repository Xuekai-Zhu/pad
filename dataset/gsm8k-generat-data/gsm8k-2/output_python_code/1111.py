def solution():
    """42 raspberries, blackberries, and blueberries were picked in total. If half of all the berries had been raspberries, and a third of the berries were blackberries, how many of them were blueberries?"""
    total = 42
    raspberries = total / 2
    blackberries = total / 3
    blueberries = total - raspberries - blackberries
    result = blueberries
    return result

print(solution())