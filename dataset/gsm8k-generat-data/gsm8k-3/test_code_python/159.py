def solution():
    """At Mario's barbershop haircuts are 50% more expensive during the weekends. If Mario paid $18 for his last haircut on Monday, how much he would have paid the day before?"""
    # Define the percentage increase in price
    weekend_increase = 50

    # Calculate the weekend price
    weekend_price = 18 * (1 + (weekend_increase/100))

    # Round the result to 2 decimal places
    result = round(weekend_price, 2)
    return result

print(solution())