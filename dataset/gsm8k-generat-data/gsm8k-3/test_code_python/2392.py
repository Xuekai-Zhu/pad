def solution():
    """John assembles computers and sells prebuilt computers as a business. The parts for the computer cost $800.  He sells the computers for 1.4 times the value of the components.  He manages to build 60 computers a month.  He has to pay $5000 a month in rent and another $3000 in non-rent extra expenses a month. How much profit does he make a month?"""
    # Define the cost of the computer components and the selling price multiplier
    COMPONENTS_COST = 800
    SELLING_PRICE_MULTIPLIER = 1.4

    # Define the number of computers built and the fixed expenses
    COMPUTERS_BUILT = 60
    RENT_EXPENSE = 5000
    EXTRA_EXPENSES = 3000

    # Calculate the revenue from selling the computers
    selling_price = COMPONENTS_COST * SELLING_PRICE_MULTIPLIER
    revenue = selling_price * COMPUTERS_BUILT

    # Calculate the total expenses
    total_expenses = RENT_EXPENSE + EXTRA_EXPENSES + (COMPONENTS_COST * COMPUTERS_BUILT)

    # Calculate the profit
    profit = revenue - total_expenses

    # Display the profit
    result = profit
    return result

print(solution())