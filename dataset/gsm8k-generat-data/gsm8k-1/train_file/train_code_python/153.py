def solution():
    """Ariella has $200 more in her son's saving account than Daniella has in her son's savings account. Ariella's account earns her simple interest at the rate of 10% per annum. If Daniella has $400, how much money will Arialla have after two years?"""
    daniella_balance = 400
    ariella_balance = daniella_balance + 200
    interest_rate = 0.1
    years = 2
    ariella_interest = ariella_balance * interest_rate * years
    ariella_total = ariella_balance + ariella_interest
    result = ariella_total
    return result

print(solution())