def solution():
    num_bracelets = 12  # Josh makes 12 bracelets
    cost_per_bracelet = 1  # The cost of supplies for each bracelet is $1
    price_per_bracelet = 1.5  # Josh sells each bracelet for $1.5

    # Calculate how much money Josh makes from selling bracelets
    total_earnings = num_bracelets * price_per_bracelet

    # Calculate how much money Josh spends on supplies
    total_cost = num_bracelets * cost_per_bracelet

    # Calculate how much money Josh has left after buying the cookies
    remaining_money = total_earnings - total_cost - 3  # We subtract $3 from the remaining money to get the cost of the cookies

    result = remaining_money
    return result

print(solution())