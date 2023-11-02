def solution():
    """Tom buys a bedroom set for $3000. He sells his old bedroom for $1000 and uses that to pay for part of the bedroom set. He then has to pay 10% a month for the bedroom set. How much does he have to pay per month?"""
    bedroom_set_cost = 3000
    old_bedroom_sale = 1000
    amount_due = bedroom_set_cost - old_bedroom_sale
    monthly_payment = amount_due * 0.1
    result = monthly_payment
    return result

print(solution())