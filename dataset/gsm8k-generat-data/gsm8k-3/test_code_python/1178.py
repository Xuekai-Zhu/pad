def solution():
    """Oula and Tona work for a delivery service company, supplying different parts of their state with milk products. They are paid $100 for each delivery made in a day. In a particular month, Oula made 96 deliveries while Tona made 3/4 times as many deliveries as Oula. Calculate their difference in pay that month."""
    # Define the payment per delivery
    PAY_PER_DELIVERY = 100

    # Calculate the number of deliveries made by Oula
    oula_deliveries = 96

    # Calculate the number of deliveries made by Tona
    tona_deliveries = oula_deliveries * 3/4

    # Calculate the payment received by Oula
    oula_payment = oula_deliveries * PAY_PER_DELIVERY

    # Calculate the payment received by Tona
    tona_payment = tona_deliveries * PAY_PER_DELIVERY

    # Calculate the difference in payment between Oula and Tona
    payment_difference = oula_payment - tona_payment

    # Display the payment difference
    result = payment_difference
    return result

print(solution())