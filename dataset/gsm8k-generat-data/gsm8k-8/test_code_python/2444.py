def solution():
    # Define the amount of money raised by each status
    bronze_money = 25 * 10
    silver_money = 50 * 7
    gold_money = 100 * 1

    # Calculate the total money raised so far
    total_money = bronze_money + silver_money + gold_money

    # Calculate the remaining money needed to reach the goal
    remaining_money = 750 - total_money

    result = remaining_money
    return result

print(solution())