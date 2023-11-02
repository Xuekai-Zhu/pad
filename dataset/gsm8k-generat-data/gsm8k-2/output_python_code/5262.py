def solution():
    """Sue and her sister buy a $2,100 car. They agree to split the cost based on the percentage of days use. Sue's sister will drive the car 4 days a week and Sue will get the rest of the days. How much does Sue have to pay?"""
    total_cost = 2100
    sister_days = 4
    sue_days = 7 - sister_days
    sister_percentage = sister_days / 7
    sue_percentage = sue_days / 7
    sue_payment = sue_percentage * total_cost
    result = sue_payment
    return result

print(solution())