def solution():
    
    # Define the hourly wage and number of hours worked
    hourly_wage = 50
    weekly_hours = 6

    # Calculate the total earnings
    total_earnings = hourly_wage * weekly_hours

    # Subtract the gas expense and the bank cost
    total_earnings -= 50
    total_earnings -= 100

    # Calculate the number of pencils that can be bought with the remaining money
    pencils_bought = 5
    pencil_cost = 10
    pens_bought = (total_earnings // pencil_cost) // pencil_cost

    # Display the number of pens bought
    result = pens_bought
    return result

print(solution())