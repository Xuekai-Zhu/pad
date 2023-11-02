def solution():
    """Roxanne bought 2 cups of lemonade for $2 each and 2 sandwiches for $2.50 each. How much change must she get from a $20 bill?"""
    cups_of_lemonade = 2
    price_of_lemonade = 2
    sandwiches = 2
    price_of_sandwich = 2.5
    total_cost = cups_of_lemonade * price_of_lemonade + sandwiches * price_of_sandwich
    amount_paid = 20
    change = amount_paid - total_cost
    result = change
    return result

print(solution())