def solution():
    milk_price = 3
    banana_price = 2
    sales_tax = 0.2  # 20% sales tax

    # Calculate the total cost of milk and bananas before tax
    total_cost_before_tax = milk_price + banana_price

    # Calculate the total cost of sales tax
    total_sales_tax = total_cost_before_tax * sales_tax

    # Calculate the total cost including tax
    total_cost = total_cost_before_tax + total_sales_tax
    result = total_cost
    return result

print(solution())