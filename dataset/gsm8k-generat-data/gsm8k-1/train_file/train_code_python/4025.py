def solution():
    """Mr. Ha owns 5 more silver dollars than Mr. Phung. Mr. Phung has 16 more silver dollars than Mr. Chiu has. If Mr. Chiu has 56 silver dollars, how many silver dollars the three have in total?"""
    chiu_silver_dollars = 56
    phung_silver_dollars = chiu_silver_dollars + 16
    ha_silver_dollars = phung_silver_dollars + 5
    total_silver_dollars = chiu_silver_dollars + phung_silver_dollars + ha_silver_dollars
    result = total_silver_dollars
    return result

print(solution())