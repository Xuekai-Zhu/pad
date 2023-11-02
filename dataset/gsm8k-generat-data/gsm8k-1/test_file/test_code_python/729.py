def solution():
    """While walking down the street with his 3 younger siblings, Greg found $20. To be fair to his siblings, he decided to split the money equally. How much money did each of them get?"""
    found_money = 20
    num_siblings = 3
    split_money = found_money / (num_siblings + 1)
    result = split_money
    return result

print(solution())