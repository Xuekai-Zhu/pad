def solution():
    """Maximoff's monthly bill is $60 per month. His monthly bill increased by thirty percent when he started working at home. How much is his total monthly bill working from home?"""
    initial_bill = 60
    percent_increase = 30
    increase_amount = initial_bill * (percent_increase / 100)
    total_bill = initial_bill + increase_amount
    result = total_bill
    return result

print(solution())