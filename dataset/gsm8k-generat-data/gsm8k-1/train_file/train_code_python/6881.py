def solution():
    """Brendan works online and is paid every week. Once he gets the money, he recharges his debit card with half of his pay. In June, he earned $5000 and bought himself a used car worth $1500. What is his total amount of remaining money at the end of the month?"""
    pay_per_week = 5000 / 4
    recharge_amount = pay_per_week / 2
    total_recharge = recharge_amount * 4
    remaining_money = (5000 - total_recharge) - 1500
    result = remaining_money
    return result

print(solution())