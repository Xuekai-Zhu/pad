def solution():
    """Jake agrees to work part of his debt off. He owed someone $100 but paid them $40 before agreeing to work off the rest. He worked for $15 an hour. How many hours did he have to work?"""
    # Define the debt and the amount Jake has already paid
    debt = 100
    paid = 40
    
    # Calculate the remaining debt
    remaining_debt = debt - paid
    
    # Calculate the number of hours Jake has to work to pay off the remaining debt
    hours = remaining_debt / 15
    
    # Display the result
    result = hours
    return result

print(solution())