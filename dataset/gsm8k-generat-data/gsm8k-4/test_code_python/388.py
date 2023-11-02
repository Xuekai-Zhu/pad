def solution():
    """John sublets his apartment to 3 people who each pay $400 per month. He rents the apartment for $900 a month. How much profit does he make in a year?"""
    # Define the number of tenants and the rent and sublet prices
    num_tenants = 3
    rent_price = 900
    sublet_price = 400

    # Calculate the total income and expenses for one month
    total_income_month = num_tenants * sublet_price
    total_expenses_month = rent_price

    # Calculate the profit for one month
    profit_month = total_income_month - total_expenses_month

    # Calculate the profit for one year
    profit_year = profit_month * 12

    # return the result
    result = profit_year
    return result

print(solution())