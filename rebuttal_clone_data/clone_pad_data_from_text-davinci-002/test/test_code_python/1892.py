def solution():
    blueberries = 30
    cranberries = 20
    raspberries = 10
    total_berries = blueberries + cranberries + raspberries
    rotten_berries = total_berries / 3
    fresh_berries = total_berries - rotten_berries
    berries_to_sell = fresh_berries / 2
    result = berries_to_sell
    return result

print(solution())