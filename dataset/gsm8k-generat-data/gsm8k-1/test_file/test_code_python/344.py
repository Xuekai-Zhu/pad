def solution():
    """A factory used to make tractors, but now makes silos. When they made tractors, they sold 10 tractors a day and made $100 per tractor. Now, they sell 5 silos a day, and make $220 per silo. What percentage more are they making per day now?"""
    tractors_sold = 10
    tractor_price = 100
    silos_sold = 5
    silo_price = 220
    tractor_revenue = tractors_sold * tractor_price
    silo_revenue = silos_sold * silo_price
    percentage_increase = ((silo_revenue - tractor_revenue) / tractor_revenue) * 100
    result = percentage_increase
    return result

print(solution())