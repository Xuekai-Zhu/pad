def solution():
    """Maximoff's monthly bill is $60 per month. His monthly bill increased by thirty percent when he started working at home. How much is his total monthly bill working from home?"""
    base_bill = 60
    increase_percent = 30
    increase_amount = base_bill * (increase_percent / 100)
    total_bill = base_bill + increase_amount
    result = total_bill
    return result

print(solution())