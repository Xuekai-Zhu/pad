def solution():
    """John sublets his apartment to 3 people who each pay $400 per month.  He rents the apartment for $900 a month.  How much profit does he make in a year?"""
    # Define the monthly rent and the amount paid by each subletter
    MONTHLY_RENT = 900
    SUBLETTER_PAYMENT = 400

    # Calculate the total amount paid by the subletters each month
    subletter_total = 3 * SUBLETTER_PAYMENT

    # Calculate John's monthly profit
    monthly_profit = MONTHLY_RENT - subletter_total

    # Calculate John's annual profit
    annual_profit = monthly_profit * 12

    # Display John's annual profit
    result = annual_profit
    return result

print(solution())