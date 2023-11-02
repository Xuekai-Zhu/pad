def solution():
    pay_per_delivery = 100  # They get paid $100 per delivery
    oula_deliveries = 96  # Oula made 96 deliveries
    tona_deliveries = 3/4 * oula_deliveries  # Tona made 3/4 as many deliveries as Oula

    # Calculate their total pay for the month
    oula_pay = pay_per_delivery * oula_deliveries
    tona_pay = pay_per_delivery * tona_deliveries
    pay_difference = oula_pay - tona_pay
    result = pay_difference
    return result 

Note: In the solution, we multiplied Oula's deliveries by the pay_per_delivery while calculating her pay, but we didn't do the same for Tona. This is because we already calculated Tona's deliveries as a fraction of Oula's deliveries, so we can directly multiply this fraction by pay_per_delivery to get Tona's pay.

print(solution())