def solution():
    """Jane is shopping for some fruit. She sees a stand of fruit advertising 10 apples for $2, and another one advertising 5 oranges for $1.50. Assuming there's no price discount for buying in bulk, how much would Jane spend in cents if she bought 12 of the cheaper of the two fruits?"""
    apple_price = 2/10  # price per apple
    orange_price = 1.5/5  # price per orange
    cheaper_fruit_price = min(apple_price, orange_price)
    cheaper_fruit_cost = cheaper_fruit_price * 12
    result = int(cheaper_fruit_cost * 100)  # convert to cents
    return result

print(solution())