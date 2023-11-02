def solution():
    """If the price of a bag of cherries is $5 when the price of a bag of olives is $7, how much would Jordyn pay for buying 50 bags of each fruit and a 10% discount?"""
    # Define the prices of cherries and olives and the number of bags
    cherry_price = 5
    olive_price = 7
    num_bags = 50

    # Calculate the total cost before discount
    total_cost = (cherry_price + olive_price) * num_bags

    # Calculate the discount amount
    discount = total_cost * 0.1

    # Calculate the total cost after discount
    total_cost -= discount

    result = total_cost
    return result

print(solution())