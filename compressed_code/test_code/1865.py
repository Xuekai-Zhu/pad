def solution():
    
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