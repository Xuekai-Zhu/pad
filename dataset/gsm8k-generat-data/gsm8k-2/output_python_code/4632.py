def solution():
    """Toby is dining out with his friend. They each order a cheeseburger for $3.65.
    He gets a milkshake for $2 and his friend gets a coke for $1.
    They split a large fries that cost $4. His friend also gets three cookies that cost $.5 each.
    The tax is $.2. They agree to split the bill.
    If Toby arrived with $15, how much change is he bringing home?"""
    cheeseburger_price = 3.65
    milkshake_price = 2
    coke_price = 1
    fries_price = 4
    cookies_price = 0.5
    tax = 0.2

    total_cost = (cheeseburger_price * 2) + milkshake_price + coke_price + fries_price + (cookies_price * 3)
    total_cost_with_tax = total_cost + (total_cost * tax)
    split_cost = total_cost_with_tax / 2
    change = 15 - split_cost
    result = change
    return result

print(solution())