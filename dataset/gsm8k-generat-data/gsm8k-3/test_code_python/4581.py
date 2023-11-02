def solution():
    """Mr. Jesiah is a dairy cow farmer with cows producing 200 gallons of milk every day. The expenses for maintenance of the dairy farm and purchase of feeds is $3000 per month. Calculate his total income in June if he sells 1 gallon of milk at $3.55."""
    # Define the daily milk production in gallons and the milk price per gallon
    DAILY_MILK_PRODUCTION = 200
    MILK_PRICE = 3.55

    # Define the expenses for maintaining and feeding the cows
    MONTHLY_EXPENSES = 3000

    # Calculate the total milk production for June
    JUNE_MILK_PRODUCTION = DAILY_MILK_PRODUCTION * 30

    # Calculate the total income from milk sales in June
    JUNE_INCOME = JUNE_MILK_PRODUCTION * MILK_PRICE

    # Calculate the net income after deducting expenses
    NET_INCOME = JUNE_INCOME - MONTHLY_EXPENSES

    # Display the net income for June
    result = NET_INCOME
    return result

print(solution())