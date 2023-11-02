def solution():
    """At a coffee shop, 7 customers order coffee at $5 each and 8 customers order tea at $4 each. How much money did the coffee shop make?"""
    coffee_customers = 7
    coffee_price = 5
    tea_customers = 8
    tea_price = 4
    total_sales = (coffee_customers * coffee_price) + (tea_customers * tea_price)
    result = total_sales
    return result

print(solution())