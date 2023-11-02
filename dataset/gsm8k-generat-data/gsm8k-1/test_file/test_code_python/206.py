def solution():
    """Sara wants to buy herself a new jacket and 2 pairs of shoes. The jacket she wants costs $30 and each pair of shoes cost $20. Sara babysits the neighbor's kids 4 times, earning $5 each time she babysits them. Her parents pay her $4 each time she mows the lawn. If Sara already had $10 saved before she started babysitting, how many times must she mow the lawn before she can afford the jacket and shoes?"""
    jacket_cost = 30
    shoe_cost = 20
    total_shoe_cost = shoe_cost * 2
    total_cost = jacket_cost + total_shoe_cost

    babysitting_earnings = 5 * 4
    lawn_mowing_earnings_per_session = 4

    total_earnings = babysitting_earnings + 10
    total_sessions_needed = (total_cost - total_earnings) / lawn_mowing_earnings_per_session

    result = total_sessions_needed
    return result

print(solution())