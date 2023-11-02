def solution():
    # Calculate the amount of money raised from each status
    bronze_money = 25 * 10  # 10 Bronze Status Families who donated $25 each
    silver_money = 50 * 7  # 7 Silver Status Families who donated $50 each
    gold_money = 100 * 1  # 1 Gold Status family who donated $100

    # Calculate the total amount raised so far
    total_money = bronze_money + silver_money + gold_money

    # Calculate the amount of money needed to reach the goal
    goal = 750
    remaining_money = goal - total_money
    result = remaining_money
    return result

print(solution())