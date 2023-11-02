def solution():
    """Heisenberg owns a pharmacy. He earned a total of $80 from 100 mg amoxicillin and $60 from 500 mg amoxicillin every week. If each capsule of 100 mg amoxicillin costs $5 and each capsule of 500 mg amoxicillin costs $2, how many capsules of amoxicillin does he sell every 2 weeks?"""
    amox_100_price = 5
    amox_500_price = 2
    weekly_amox_100_profit = 80
    weekly_amox_500_profit = 60
    weekly_amox_100_qty = weekly_amox_100_profit / amox_100_price
    weekly_amox_500_qty = weekly_amox_500_profit / amox_500_price
    total_qty = (weekly_amox_100_qty + weekly_amox_500_qty) * 2
    result = total_qty
    return result

print(solution())