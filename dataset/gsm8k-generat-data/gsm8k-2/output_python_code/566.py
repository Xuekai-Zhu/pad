def solution():
    """ Lilith originally had five dozen water bottles that she needed to sell at $2 each to get exactly enough money to buy her friend a birthday gift. However, at the store, Lilith realized she could not sell at $2 because the regular price was $1.85 per water bottle in her town, and she had to reduce her price to $1.85 as well to sell her water bottles. Calculate the total amount of money Lilith will have to find to buy her friend the birthday gift after selling her water bottles at the reduced cost. """
    original_price = 2
    reduced_price = 1.85
    bottles = 5 * 12
    original_revenue = original_price * bottles
    reduced_revenue = reduced_price * bottles
    difference = original_revenue - reduced_revenue
    gift_cost = difference
    result = gift_cost
    return result

print(solution())