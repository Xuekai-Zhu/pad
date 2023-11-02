def solution():
    """Scott wants to buy a skateboard. To make money, Scott sold berry smoothies for $3 a cup and cakes for $2 each. He sold 40 cups of smoothies and 18 cakes. How much money did he make?"""
    smoothie_price = 3
    cake_price = 2
    num_smoothies = 40
    num_cakes = 18
    total_money = (smoothie_price * num_smoothies) + (cake_price * num_cakes)
    result = total_money
    return result

print(solution())