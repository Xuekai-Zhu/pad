def solution():
    advertising_cost = 1000  # James pays $1000 for advertising
    customers_brought = 100  # The advertising brought 100 customers to his site
    conversion_rate = 0.8  # 80% of those customers bought something

    # Calculate the total revenue generated from the advertising
    revenue_generated = customers_brought * conversion_rate * 25  # Each customer who bought something spent $25

    # Calculate the profit gained from the advertising
    profit = revenue_generated - advertising_cost
    result = profit
    return result

print(solution())