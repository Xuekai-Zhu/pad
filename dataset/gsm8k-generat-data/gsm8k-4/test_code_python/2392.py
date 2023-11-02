def solution():
    """John assembles computers and sells prebuilt computers as a business. The parts for the computer cost $800. He sells the computers for 1.4 times the value of the components. He manages to build 60 computers a month. He has to pay $5000 a month in rent and another $3000 in non-rent extra expenses a month. How much profit does he make a month?"""
    # Define the cost of parts, the selling price and the quantity of computers
    parts_cost = 800
    selling_price = 1.4 * parts_cost
    computers = 60

    # Calculate the revenue
    revenue = selling_price * computers

    # Calculate the total expenses
    expenses = 5000 + 3000 + parts_cost * computers

    # Calculate the profit
    profit = revenue - expenses

    # return the result
    result = profit
    return result

print(solution())