def solution():
    """Jim decides to open up a bike shop. The most common repair he does is fixing bike tires. He charges $20 for this and it cost him $5 in parts. 
    In one month Jim does 300 of these repairs. He also does 2 more complex repairs for $300 each and cost $50 in parts. 
    He also sells $2000 profit worth of things from his retail shop. If rent and other fixed expense for the shop is $4000 a month how much profit did the shop make?"""
    
    # Define the cost and revenue for tire repairs
    tire_repair_cost = 5
    tire_repair_revenue = 20
    tire_repairs = 300

    # Calculate the profit from tire repairs
    tire_repair_profit = (tire_repair_revenue - tire_repair_cost) * tire_repairs

    # Define the cost and revenue for complex repairs
    complex_repair_cost = 50
    complex_repair_revenue = 300
    complex_repairs = 2

    # Calculate the profit from complex repairs
    complex_repair_profit = (complex_repair_revenue - complex_repair_cost) * complex_repairs

    # Calculate the total profit from repairs
    total_repair_profit = tire_repair_profit + complex_repair_profit

    # Calculate the profit from retail sales
    retail_profit = 2000

    # Define the fixed expenses
    fixed_expenses = 4000

    # Calculate the total profit
    total_profit = total_repair_profit + retail_profit - fixed_expenses

    # Return the total profit
    return total_profit

print(solution())