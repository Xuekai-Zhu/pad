def solution():
    # Calculate the revenue from selling amulets
    revenue = (25 * 40 * 2)  # 25 amulets sold each day, $40 per amulet, sold for 2 days

    # Calculate the cost of making the amulets
    cost = (25 * 30 * 2)  # 25 amulets made each day, $30 cost per amulet, made for 2 days

    # Calculate the faire fee which is 10% of the revenue
    faire_fee = revenue * 0.1

    # Calculate the profit made by Dirk
    profit = revenue - cost - faire_fee
    result = profit
    return result

print(solution())