def solution():
    """James gets a job selling used cars. He sold 10 cars that cost $25,000 each. The company paid 30% of that price to acquire the cars. He got a 10% commission on the profits. How much did he make?"""
    cars_sold = 10
    cost_per_car = 25000
    acquisition_percent = 0.3
    commission_percent = 0.1
    
    acquisition_cost = cars_sold * cost_per_car * acquisition_percent
    sale_price = cars_sold * cost_per_car
    profit = sale_price - acquisition_cost
    commission = profit * commission_percent
    total_income = commission
    
    return total_income

print(solution())