def solution():
    blueberries = 30
    cranberries = 20
    raspberries = 10

    total_berrie = blueberries + cranberries + raspberries

    rotten_berrie = total_berrie / 3

    fresh_berrie = total_berrie - rotten_berrie

    kept_berrie = fresh_berrie / 2

    sell_berrie = fresh_berrie - kept_berrie
    result = sell_berrie
    return result

print(solution())