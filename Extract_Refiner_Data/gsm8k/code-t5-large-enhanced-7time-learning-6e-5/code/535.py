def solution():
    
    # Define the tip percentage and the amount paid
    tip_percentage = 20
    amount_paid = 50

    # Calculate the amount of the tip
    tip_amount = amount_paid * (tip_percentage / 100)

    # Calculate the total amount paid
    total_paid = amount_paid + tip_amount

    # Display the total amount paid
    result = total_paid
    return result

print(solution())