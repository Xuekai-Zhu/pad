def solution():
    """Jake agrees to work part of his debt off.  He owed someone $100 but paid them $40 before agreeing to work off the rest.   He worked for $15 an hour.  How many hours did he have to work?"""
    # Define the amount owed and the amount already paid
    AMOUNT_OWED = 100
    AMOUNT_PAID = 40

    # Calculate the remaining amount owed
    remaining_amount = AMOUNT_OWED - AMOUNT_PAID

    # Calculate the number of hours Jake has to work to pay off the remaining amount
    hours_worked = remaining_amount / 15

    # Display the number of hours worked
    result = hours_worked
    return result

print(solution())