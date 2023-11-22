def solution():
    
    # Define the initial amount of money in Sally's bank account
    initial_amount = 200

    # Define the amount of money in Sally's bank account after the weekly wage
    bank_amount = 420

    # Define the weekly wage amount
    weekly_wage = 300

    # Calculate the amount of money Sally had before the weekly wage
    initial_amount = initial_amount + bank_amount

    # Calculate the amount of money Sally had after the weekly wage
    final_amount = initial_amount - weekly_wage

    # Display the amount of money Sally had withheld
    result = final_amount
    return result

print(solution())