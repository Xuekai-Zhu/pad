def solution():
    """Scott wants to buy a skateboard. To make money, Scott sold berry smoothies for $3 a cup and cakes for $2 each. He sold 40 cups of smoothies and 18 cakes. How much money did he make?"""
    smoothies_price = 3
    cakes_price = 2
    smoothies_sold = 40
    cakes_sold = 18
    total_money = (smoothies_price * smoothies_sold) + (cakes_price * cakes_sold)
    result = total_money
    return result

print(solution())