def solution():
    """Ariella has $200 more in her son's saving account than Daniella has in her son's savings account. Ariella's account earns her simple interest at the rate of 10% per annum. If Daniella has $400, how much money will Ariella have after two years?"""
    daniella_savings = 400
    ariella_savings = daniella_savings + 200
    interest_rate = 0.1
    ariella_interest = ariella_savings * interest_rate * 2
    total_ariella_savings = ariella_savings + ariella_interest
    result = total_ariella_savings
    return result

print(solution())