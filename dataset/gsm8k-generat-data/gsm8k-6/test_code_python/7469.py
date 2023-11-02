def solution():
    # Calculate the cost of supplies for 12 bracelets
    supply_cost = 12 * 1  # it costs $1 for supplies for each bracelet
    total_sale = 12 * 1.5   # he sells each bracelet for $1.5
    revenue = total_sale - supply_cost  # the revenue from selling the bracelets
    cookie_cost = revenue - 3  # Josh has $3 left after buying the cookies
    result = cookie_cost
    return result

print(solution())