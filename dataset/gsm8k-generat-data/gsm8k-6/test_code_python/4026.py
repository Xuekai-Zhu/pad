def solution():
    # Find the number of silver dollars owned by Mr. Chiu, Mr. Phung, and Mr. Ha
    chiu_silver_dollars = 56
    phung_silver_dollars = chiu_silver_dollars + 16
    ha_silver_dollars = phung_silver_dollars + 5

    # Calculate the total number of silver dollars
    total_silver_dollars = chiu_silver_dollars + phung_silver_dollars + ha_silver_dollars
    result = total_silver_dollars
    return result

print(solution())