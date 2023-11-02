def solution():
    """Ariella has $200 more in her son's saving account than Daniella has in her son's savings account. Ariella's account earns her simple interest at the rate of 10% per annum. If Daniella has $400, how much money will Ariella have after two years?"""
    ariella_initial_amount = 200
    daniella_initial_amount = 400
    interest_rate = 10
    time = 2
    ariella_amount = ariella_initial_amount + (ariella_initial_amount * interest_rate * time / 100)
    result = ariella_amount
    return result

print(solution())