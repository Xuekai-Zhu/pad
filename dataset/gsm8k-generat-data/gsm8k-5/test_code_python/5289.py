def solution():
    papers_per_week = 7 * 250  # John was supposed to deliver 250 papers per day, 7 days a week
    weight_mon_sat = 8  # Monday-Saturday papers weigh 8 ounces each
    weight_sun = weight_mon_sat * 2  # Sunday papers weigh twice as much as the Monday-Saturday papers
    total_weight = papers_per_week * (weight_mon_sat * 6 + weight_sun) * 10  # John didn't deliver papers for 10 weeks

    # Convert total weight to tons and calculate how much John made
    weight_in_tons = total_weight / 32000  # 32,000 ounces in a ton
    cash_made = weight_in_tons * 20  # John makes $20 per ton of paper
    result = cash_made
    return result

print(solution())