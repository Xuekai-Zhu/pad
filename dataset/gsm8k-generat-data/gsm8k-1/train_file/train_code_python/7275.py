def solution():
    """The bowl of fruit contains apples, pears, and bananas. There are two more pears than apples, and three more bananas than pears. If the bowl contains 19 pieces of fruit, how many bananas does it contain?"""
    total_fruit = 19
    apples = x
    pears = x+2
    bananas = (x+2)+3
    total_pieces = apples + pears + bananas
    bananas = total_fruit - total_pieces + bananas
    result = bananas
    return result

print(solution())