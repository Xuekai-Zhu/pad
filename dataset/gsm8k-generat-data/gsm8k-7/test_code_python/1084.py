def solution():
    cost_per_person = 20 + 5  # $25
    total_cost = cost_per_person * 2  # $50

    tip_percent = 20  # 20% tip
    tip_amount = total_cost * (tip_percent / 100)  # $10 tip

    billy_share = total_cost / 2  # Billy pays $25
    billy_tip_share = tip_amount * 0.8 / 2  # Billy wants to cover 80% of a 20% tip for two people
    billy_total = billy_share + billy_tip_share
    result = billy_total
    return result

print(solution())