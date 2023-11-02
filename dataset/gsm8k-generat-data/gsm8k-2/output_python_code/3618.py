def solution():
    """In a restaurant, one cup of coffee is $6 and a piece of cheesecake $10. When buying them together, the client gets a 25% discount. What is the final price of such a set?"""
    coffee_price = 6
    cheesecake_price = 10
    discount = 0.25
    total_price = coffee_price + cheesecake_price
    discounted_price = total_price - (total_price * discount)
    result = discounted_price
    return result

print(solution())