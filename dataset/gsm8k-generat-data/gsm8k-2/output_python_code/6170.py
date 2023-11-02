def solution():
    """Ted needs to purchase 5 bananas and 10 oranges. If bananas cost $2 each and oranges cost $1.50 each. How much money does Ted need to purchase 5 bananas and 10 oranges?"""
    banana_price = 2
    orange_price = 1.5
    num_bananas = 5
    num_oranges = 10
    total_cost = (banana_price * num_bananas) + (orange_price * num_oranges)
    result = total_cost
    return result

print(solution())