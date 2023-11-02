def solution():
    """At a coffee shop, 7 customers order coffee at $5 each and 8 customers order tea at $4 each. How much money did the coffee shop make?"""
    coffee_price = 5
    tea_price = 4
    num_coffee = 7
    num_tea = 8
    total_sales = (coffee_price * num_coffee) + (tea_price * num_tea)
    result = total_sales
    return result

print(solution())