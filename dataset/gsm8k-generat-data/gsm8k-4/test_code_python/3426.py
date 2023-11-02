def solution():
    """Lorie has 2 pieces of $100 bills. He requested to change one piece of the $100 bills into $50 bills. Half of the remaining $100 bill is changed to $10 bills while the rest is changed to $5 bills. How many pieces of bills will she have?"""
    # Define the initial number of $100 bills
    initial_100_bills = 2

    # Change one $100 bill to $50 bills
    remaining_bills = initial_100_bills - 1
    fifty_bills = 2

    # Change half of the remaining $100 bill to $10 bills
    remaining_bills = remaining_bills/2
    ten_bills = remaining_bills

    # Change the rest of the $100 bill to $5 bills
    five_bills = remaining_bills

    # Calculate the total number of bills
    total_bills = initial_100_bills + fifty_bills + ten_bills + five_bills

    result = total_bills
    return result

print(solution())