def solution():
    """John assembles computers and sells prebuilt computers as a business. The parts for the computer cost $800. He sells the computers for 1.4 times the value of the components. He manages to build 60 computers a month. He has to pay $5000 a month in rent and another $3000 in non-rent extra expenses a month. How much profit does he make a month?"""
    parts_cost = 800
    sell_price = 1.4 * parts_cost
    num_computers = 60
    rent_cost = 5000
    other_expenses = 3000
    total_income = sell_price * num_computers
    total_expenses = parts_cost * num_computers + rent_cost + other_expenses
    profit = total_income - total_expenses
    result = profit
    return result

print(solution())