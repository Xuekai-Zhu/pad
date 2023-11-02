def solution():
    """Ursula bought five hot dogs at $1.50 each and three salads at $2.50 each. If she had two $10 bills, how much change did she get back?"""
    hotdog_price = 1.5
    salad_price = 2.5
    num_hotdogs = 5
    num_salads = 3
    total_cost = (hotdog_price * num_hotdogs) + (salad_price * num_salads)
    paid_amount = 10 * 2
    change = paid_amount - total_cost
    result = change
    return result

print(solution())