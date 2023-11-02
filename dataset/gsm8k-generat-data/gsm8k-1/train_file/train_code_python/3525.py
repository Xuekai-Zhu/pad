def solution():
    """Jane is shopping for some fruit. She sees a stand of fruit advertising 10 apples for $2, and another one advertising 5 oranges for $1.50. Assuming there's no price discount for buying in bulk, how much would Jane spend in cents if she bought 12 of the cheaper of the two fruits?"""
    apples_price = 200 / 10 # price per apple in cents
    oranges_price = 150 / 5 # price per orange in cents
    cheaper_price = min(apples_price, oranges_price)
    num_fruits = 12
    total_cost = cheaper_price * num_fruits
    result = total_cost
    return result

print(solution())