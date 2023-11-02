def solution():
    """John assembles computers and sells prebuilt computers as a business. The parts for the computer cost $800. He sells the computers for 1.4 times the value of the components. He manages to build 60 computers a month. He has to pay $5000 a month in rent and another $3000 in non-rent extra expenses a month. How much profit does he make a month?"""
    components_cost = 800
    sale_price = 1.4 * components_cost
    num_computers = 60
    revenue = sale_price * num_computers
    rent = 5000
    other_expenses = 3000
    total_expenses = rent + other_expenses
    profit = revenue - total_expenses
    result = profit
    return result

print(solution())