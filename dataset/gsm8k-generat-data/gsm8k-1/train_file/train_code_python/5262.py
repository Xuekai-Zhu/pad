def solution():
    """Sue and her sister buy a $2,100 car. They agree to split the cost based on the percentage of days use. Sue's sister will drive the car 4 days a week and Sue will get the rest of the days. How much does Sue have to pay?"""
    total_cost = 2100
    sister_days = 4
    sue_days = 7 - sister_days
    sister_share = (sister_days / 7) * total_cost
    sue_share = total_cost - sister_share
    result = sue_share
    return result

print(solution())