def solution():
    # Define the number of deliveries made by Oula
    oula_deliveries = 96

    # Calculate the number of deliveries made by Tona
    tona_deliveries = 3/4 * oula_deliveries

    # Calculate the pay earned by Oula and Tona
    oula_pay = oula_deliveries * 100
    tona_pay = tona_deliveries * 100

    # Calculate the difference in pay
    pay_difference = abs(oula_pay - tona_pay)
    result = pay_difference
    return result

print(solution())