def solution():
    """Jim decides to open up a bike shop.  The most common repair he does is fixing bike tires.  He charges $20 for this and it cost him $5 in parts.  In one month Jim does 300 of these repairs.  He also does 2 more complex repairs for $300 each and cost $50 in parts.  He also sells $2000 profit worth of things from his retail shop.  If rent and other fixed expense for the shop is $4000 a month how much profit did the shop make?"""
    # Calculate profit from tire repairs
    tire_repairs_income = 20 * 300
    tire_repairs_expense = 5 * 300
    tire_repairs_profit = tire_repairs_income - tire_repairs_expense

    # Calculate profit from complex repairs
    complex_repairs_income = 2 * 300
    complex_repairs_expense = 2 * 50
    complex_repairs_profit = complex_repairs_income - complex_repairs_expense

    # Calculate profit from retail sales
    retail_profit = 2000

    # Calculate total profit and subtract fixed expenses
    total_profit = tire_repairs_profit + complex_repairs_profit + retail_profit - 4000

    # Display the total profit
    result = total_profit
    return result

print(solution())