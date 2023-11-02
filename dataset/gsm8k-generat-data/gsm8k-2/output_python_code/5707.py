def solution():
    """Reuben opens a sandwich shop selling his namesake sandwich and pastrami sandwiches. Pastrami cost $2 more than the Reuben. He sells 10 Reubens and 5 Pastrami sandwiches and earns $55. How much does a pastrami sandwich cost?"""
    reuben_price = x
    pastrami_price = x + 2
    reuben_count = 10
    pastrami_count = 5
    total_earnings = 55
    total_reubens_cost = reuben_price * reuben_count
    total_pastrami_cost = pastrami_price * pastrami_count
    total_cost = total_reubens_cost + total_pastrami_cost
    pastrami_price = (total_earnings - total_reubens_cost) / pastrami_count
    result = pastrami_price
    return result

print(solution())