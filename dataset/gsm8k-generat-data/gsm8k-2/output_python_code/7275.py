def solution():
    """The bowl of fruit contains apples, pears, and bananas. There are two more pears than apples, and three more bananas than pears.
    If the bowl contains 19 pieces of fruit, how many bananas does it contain?"""
    total_fruit = 19
    apples = a
    pears = a + 2
    bananas = pears + 3
    fruits_sum = apples + pears + bananas
    bananas_num = total_fruit - fruits_sum + bananas
    result = bananas_num
    return result

print(solution())