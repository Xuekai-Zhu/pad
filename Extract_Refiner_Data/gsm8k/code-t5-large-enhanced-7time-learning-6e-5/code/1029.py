def solution():
    
    # Define the number of days and the hourly wage of the court case
    days = 3
    hourly_wage = 15

    # Calculate the total hours spent on the court case
    total_hours = 6 * days

    # Calculate the total amount Melissa will pay for parking each day
    parking_cost = 3 * days

    # Calculate Melissa's total pay for the court case
    court_pay = hourly_wage * total_hours

    # Calculate Melissa's total pay for parking
    parking_pay = parking_cost * total_hours

    # Calculate Melissa's net pay per hour after expenses
    net_pay = court_pay - parking_pay

    # Display Melissa's net pay per hour after expenses
    result = net_pay
    return result

print(solution())