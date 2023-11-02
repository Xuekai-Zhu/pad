def solution():
    """In the cafeteria, Athena wants to buy snacks for her friends. She bought 3 sandwiches at $3 each and 2 fruit drinks at $2.5 each. How much did she spend in all?"""
    sandwiches_bought = 3
    sandwich_price = 3
    drinks_bought = 2
    drink_price = 2.5
    total_spent = (sandwiches_bought * sandwich_price) + (drinks_bought * drink_price)
    result = total_spent
    return result

print(solution())