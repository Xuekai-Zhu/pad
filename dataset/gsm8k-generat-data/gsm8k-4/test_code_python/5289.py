def solution():
    """John decides to stop delivering the newspapers he is supposed to deliver and instead steals them to recycle them for cash. The Monday-Saturday papers weigh 8 ounces each. The Sunday paper weighs twice as much. He is supposed to deliver 250 papers a day. He doesn't deliver them for 10 weeks. If one ton of paper recycles for $20, how much did he make?"""
    # Calculate the weight of Monday-Saturday papers for one day
    mon_sat_weight = 8 * 6

    # Calculate the weight of Sunday paper for one day
    sun_weight = 16

    # Calculate the total weight of papers for one day
    total_weight = mon_sat_weight + sun_weight

    # Calculate the total weight of papers for 10 weeks
    total_weight_10_weeks = total_weight * 250 * 7 * 10

    # Convert the total weight from ounces to tons
    total_weight_tons = total_weight_10_weeks / 32000

    # Calculate the total amount of money made by recycling the papers
    total_money = total_weight_tons * 20

    result = round(total_money)
    return result

print(solution())