def solution():
    """
    A taco truck buys 100 pounds of beef. They use .25 pounds of beef per taco. If they sell each taco for $2 and each taco takes $1.5 to make, how much profit did they make if they used all the beef?
    """
    beef_in_pounds = 100
    beef_per_taco = 0.25
    tacos = beef_in_pounds / beef_per_taco
    taco_price = 2
    taco_cost = 1.5
    total_revenue = tacos * taco_price
    total_cost = tacos * taco_cost
    total_profit = total_revenue - total_cost
    result = total_profit
    return result

print(solution())