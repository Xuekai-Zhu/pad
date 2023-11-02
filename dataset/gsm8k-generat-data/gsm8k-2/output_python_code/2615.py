def solution():
    """Don buys recyclable bottles in a small town. Shop A normally sells him 150 bottles, shop B sells him 180 bottles and Shop C sells him the rest. How many bottles does Don buy from Shop C if he is capable of buying only 550 bottles?"""
    shop_a_bottles = 150
    shop_b_bottles = 180
    total_bottles = 550
    shop_c_bottles = total_bottles - shop_a_bottles - shop_b_bottles
    result = shop_c_bottles
    return result

print(solution())