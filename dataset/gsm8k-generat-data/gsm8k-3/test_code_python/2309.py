def solution():
    """A new factory opens up and hires 20 people to make t-shirts.  Each person makes on average 20 shirts per day during their 8-hour shift.  The employees each get paid $12 an hour plus $5 per shirt they make.  The company sells shirts for $35 each.   Nonemployee expenses come out to $1000 a day.  How much does the company make in profits per day?"""
    # Define the number of employees, average number of shirts made per employee per day, and selling price per shirt
    NUM_EMPLOYEES = 20
    AVERAGE_SHIRTS_PER_EMPLOYEE = 20
    SELLING_PRICE_PER_SHIRT = 35

    # Define the hourly wage and payment per shirt made per employee
    HOURLY_WAGE = 12
    PAYMENT_PER_SHIRT = 5

    # Calculate the cost of labor per day
    labor_cost = NUM_EMPLOYEES * HOURLY_WAGE * 8

    # Calculate the payment per shirt made by each employee per day
    payment_per_employee = AVERAGE_SHIRTS_PER_EMPLOYEE * PAYMENT_PER_SHIRT

    # Calculate the total payment to all employees per day
    total_payment = NUM_EMPLOYEES * payment_per_employee

    # Calculate the total revenue from selling all the shirts made by the employees
    total_revenue = NUM_EMPLOYEES * AVERAGE_SHIRTS_PER_EMPLOYEE * SELLING_PRICE_PER_SHIRT

    # Define the total nonemployee expenses per day
    NONEMPLOYEE_EXPENSES = 1000

    # Calculate the total profit per day
    total_profit = total_revenue - (labor_cost + total_payment + NONEMPLOYEE_EXPENSES)

    # Display the total profit
    result = total_profit
    return result

print(solution())