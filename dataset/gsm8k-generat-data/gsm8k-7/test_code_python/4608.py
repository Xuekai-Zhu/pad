def solution():
    contest_fee = 10
    num_drums_for_money = 200
    money_per_hit = 0.025
    lost_money = 7.5

    # Calculate the total money Juanita earned
    total_money = lost_money + contest_fee

    # Calculate the number of drums Juanita hit to earn that money
    num_drums_hit = (total_money / money_per_hit) - num_drums_for_money
    result = num_drums_hit
    return result

print(solution())