def solution():
    """Chris’s internet bill is $45 per month for 100 GB and $0.25 for every 1 GB over. His bill for this month is $65. How many GB over was Chris charged for on this bill?"""
    base_price = 45
    extra_price = 0.25
    total_price = 65
    data_limit = 100
    data_used = (total_price - base_price) / extra_price
    data_over = data_used - data_limit
    result = data_over
    return result

print(solution())