def solution():
    """Oula and Tona work for a delivery service company, supplying different parts of their state with milk products. They are paid $100 for each delivery made in a day. In a particular month, Oula made 96 deliveries while Tona made 3/4 times as many deliveries as Oula. Calculate their difference in pay that month."""
    # Define the pay rate per delivery
    pay_rate = 100

    # Calculate the number of deliveries made by Oula
    oula_deliveries = 96

    # Calculate the number of deliveries made by Tona
    tona_deliveries = 3/4 * oula_deliveries

    # Calculate the pay earned by Oula
    oula_pay = oula_deliveries * pay_rate

    # Calculate the pay earned by Tona
    tona_pay = tona_deliveries * pay_rate

    # Calculate the difference in pay between Oula and Tona
    pay_difference = oula_pay - tona_pay

    # Return the result
    result = pay_difference
    return result

print(solution())