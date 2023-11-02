def solution():
    chiu_dollars = 56  # Mr. Chiu has 56 silver dollars
    phung_dollars = chiu_dollars + 16  # Mr. Phung has 16 more silver dollars than Mr. Chiu
    ha_dollars = phung_dollars + 5  # Mr. Ha has 5 more silver dollars than Mr. Phung

    # Calculate the total number of silver dollars the three have in total
    total_dollars = chiu_dollars + phung_dollars + ha_dollars
    result = total_dollars
    return result

print(solution())