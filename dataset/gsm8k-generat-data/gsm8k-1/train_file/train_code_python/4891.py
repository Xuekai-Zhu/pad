def solution():
    """Liam wants to go to Paris, but first, he has to pay his bills. His trip costs $7,000, and his bills cost $3,500. Knowing that Liam has saved $500/month for 2 years, how much money will he have left after paying his bills?"""
    saved_per_month = 500
    months_saved = 24
    total_saved = saved_per_month * months_saved
    bills_cost = 3500
    trip_cost = 7000
    remaining_money = total_saved - (bills_cost + trip_cost)
    result = remaining_money
    return result

print(solution())