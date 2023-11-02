def solution():
    """If the price of a bag of cherries is $5 when the price of a bag of olives is $7, how much would Jordyn pay for buying 50 bags of each fruit and a 10% discount?"""
    cherry_price = 5
    olive_price = 7
    num_bags = 50
    total_cost = (cherry_price + olive_price) * num_bags
    discount = total_cost * 0.1
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())