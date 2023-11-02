def solution():
    crates = 3
    crate_capacity = 20
    rotten_tomatoes = 3
    total_tomatoes = crates * crate_capacity
    good_tomatoes = total_tomatoes - rotten_tomatoes
    price_per_kilo = 6
    total_revenue = good_tomatoes * price_per_kilo
    initial_cost = crates * 110
    profit = total_revenue - initial_cost
    result = profit
    return result

print(solution())