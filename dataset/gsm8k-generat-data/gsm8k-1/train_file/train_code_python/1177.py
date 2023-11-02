def solution():
    """Oula and Tona work for a delivery service company, supplying different parts of their state with milk products. They are paid $100 for each delivery made in a day. In a particular month, Oula made 96 deliveries while Tona made 3/4 times as many deliveries as Oula. Calculate their difference in pay that month."""
    oula_deliveries = 96
    tona_deliveries = oula_deliveries * 3/4
    oula_pay = oula_deliveries * 100
    tona_pay = tona_deliveries * 100
    difference = tona_pay - oula_pay
    result = difference
    return result

print(solution())