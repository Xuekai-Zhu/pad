def solution():
    """A banana tree has 100 bananas left after Raj cut some bananas from it. If Raj has eaten 70 bananas and has twice as many remaining in his basket, how many bananas were on the tree initially?"""
    bananas_left = 100
    bananas_eaten = 70
    bananas_remaining = bananas_left - bananas_eaten
    initial_bananas = bananas_remaining * 2
    result = initial_bananas
    return result

print(solution())