def solution():
    """John has to hire a lawyer. He pays $1000 upfront. He then gets charged $100 per hour. The lawyer has to work 50 hours in court time. It takes 2 times that long in prep time. His brother pays half the fee. How much did John pay?"""
    upfront_payment = 1000
    hourly_rate = 100
    court_time = 50
    prep_time = court_time * 2
    total_hours = court_time + prep_time
    total_cost = upfront_payment + (total_hours * hourly_rate)
    john_share = total_cost * 0.5
    result = john_share
    return result

print(solution())