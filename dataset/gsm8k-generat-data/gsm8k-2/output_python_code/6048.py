def solution():
    """If the price of a bag of cherries is $5 when the price of a bag of olives is $7, how much would Jordyn pay for buying 50 bags of each fruit and a 10% discount?"""
    cherries_price = 5
    olives_price = 7
    num_bags = 50
    total_price = (cherries_price + olives_price) * num_bags
    discount = 0.1 * total_price
    final_price = total_price - discount
    result = final_price
    return result

print(solution())