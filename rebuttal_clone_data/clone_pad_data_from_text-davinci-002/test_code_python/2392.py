def solution():
    cost_of_computer = 800
    markup = 1.4
    selling_price = cost_of_computer * markup
    computers_sold_month = 60
    monthly_revenue = computers_sold_month * selling_price
    monthly_rent = 5000
    monthly_extra_expenses = 3000
    monthly_profit = monthly_revenue - (monthly_rent + monthly_extra_expenses)
    result = monthly_profit
    return result

print(solution())