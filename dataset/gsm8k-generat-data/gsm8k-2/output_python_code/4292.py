def solution():
    """At a CD store, 40% of the CDs cost $10 each, and the rest cost $5 each. Prince bought half the CDs sold at $10 each, and all of the CDs sold at $5 each. If the total number of CDs was 200, how much money did Prince spend on buying the CDs?"""
    total_cds = 200
    price_of_10_cds = 10
    price_of_5_cds = 5
    num_10_cds = total_cds * 0.4
    num_5_cds = total_cds - num_10_cds
    num_half_10_cds = num_10_cds / 2
    num_other_half_10_cds = num_half_10_cds
    total_cost = (num_half_10_cds * price_of_10_cds) + (num_other_half_10_cds * price_of_10_cds) + (num_5_cds * price_of_5_cds)
    result = total_cost
    return result

print(solution())