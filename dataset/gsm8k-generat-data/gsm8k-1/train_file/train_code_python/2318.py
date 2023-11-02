def solution():
    """Mr. Mayer bought Corgi dogs for $1000 each. He plans to sell them with a 30% profit. If one of his friends wants to buy two dogs, how much should his friend pay?"""
    dog_cost = 1000
    profit_percent = 30
    selling_price = dog_cost + (dog_cost * (profit_percent / 100))
    quantity = 2
    total_cost = selling_price * quantity
    result = total_cost
    return result

print(solution())