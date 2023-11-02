def solution():
    """Ian spent half the money he made on doing online surveys. If he worked 8 hours doing surveys and on average he's able to earn $18 per hour doing surveys, how much money does he have left?"""
    hours = 8
    hourly_rate = 18
    total_earning = hours * hourly_rate
    money_spent = total_earning / 2
    remaining_money = total_earning - money_spent
    result = remaining_money
    return result

print(solution())