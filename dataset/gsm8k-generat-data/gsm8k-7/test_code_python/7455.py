def solution():
    tire_repair_fee = 20
    tire_repair_parts_cost = 5
    num_tire_repairs = 300

    complex_repair_fee = 300
    complex_repair_parts_cost = 50
    num_complex_repairs = 2

    retail_sales = 2000

    fixed_expenses = 4000

    # Calculate total revenue from tire repairs
    tire_repair_revenue = tire_repair_fee * num_tire_repairs

    # Calculate total cost of tire repairs
    tire_repair_cost = tire_repair_parts_cost * num_tire_repairs

    # Calculate total revenue from complex repairs
    complex_repair_revenue = complex_repair_fee * num_complex_repairs

    # Calculate total cost of complex repairs
    complex_repair_cost = complex_repair_parts_cost * num_complex_repairs

    # Calculate total profit from all repairs
    total_profit_from_repairs = (tire_repair_revenue + complex_repair_revenue) - (tire_repair_cost + complex_repair_cost)

    # Calculate total profit from retail sales
    total_profit_from_sales = retail_sales

    # Calculate total profit of the shop
    total_profit = total_profit_from_repairs + total_profit_from_sales - fixed_expenses

    result = total_profit
    return result

print(solution())