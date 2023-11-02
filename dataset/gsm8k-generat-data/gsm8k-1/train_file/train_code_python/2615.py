def solution():
    """Don buys recyclable bottles in a small town. Shop A normally sells him 150 bottles, shop B sells him 180 bottles and Shop C sells him the rest.
    How many bottles does Don buy from Shop C if he is capable of buying only 550 bottles?"""
    bottles_a = 150
    bottles_b = 180
    total_bottles = 550
    bottles_c = total_bottles - bottles_a - bottles_b
    result = bottles_c
    return result

print(solution())