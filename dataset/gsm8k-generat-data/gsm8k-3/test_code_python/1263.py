def solution():
    """Phil has a coin collection he likes to add to. He started with 50 state quarters his parents gave him. Over the next year he doubled this. The following year he collected 3 each month. The year after that he collected 1 every third month. The year after that he lost a quarter of them when he misplaced his collection. How many did he have left after losing some?"""
    # Phil's initial collection
    collection = 50

    # The next year he doubled his collection
    collection *= 2

    # The following year he collected 3 each month
    collection += 3 * 12

    # The year after that he collected 1 every third month
    collection += 4 * (1/3)

    # The year after that he lost a quarter of his collection
    collection *= (3/4)

    result = collection
    return result

print(solution())