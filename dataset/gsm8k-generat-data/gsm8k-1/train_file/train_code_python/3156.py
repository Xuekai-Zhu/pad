def solution():
    """Chris’s internet bill is $45 per month for 100 GB and $0.25 for every 1 GB over. His bill for this month is $65. How many GB over was Chris charged for on this bill?"""
    base_cost = 45
    overage_cost = 0.25
    total_cost = 65
    included_gb = 100
    over_gb = (total_cost - base_cost) / overage_cost
    overage = over_gb - included_gb
    result = overage
    return result

print(solution())