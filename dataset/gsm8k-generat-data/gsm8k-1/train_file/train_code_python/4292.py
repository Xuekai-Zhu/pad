def solution():
    """At a CD store, 40% of the CDs cost $10 each, and the rest cost $5 each. Prince bought half the CDs sold at $10 each, and all of the CDs sold at $5 each. If the total number of CDs was 200, how much money did Prince spend on buying the CDs?"""
    total_cds = 200
    percent_expensive = 40
    cds_expensive = total_cds * (percent_expensive / 100)
    cds_cheap = total_cds - cds_expensive
    cds_expensive_bought = cds_expensive / 2
    cost_expensive = 10
    cost_cheap = 5
    total_cost = (cds_expensive_bought * cost_expensive) + (cds_cheap * cost_cheap)
    result = total_cost
    return result

print(solution())