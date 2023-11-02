def solution():
    """Mildred and Candice went to the market. Mildred spent $25 while Candice spent $35. If their mom gave them $100 to spend, how much will be left with them after spending?"""
    # Define the amounts spent by Mildred and Candice
    mildred_spent = 25
    candice_spent = 35

    # Define the total amount given to them by their mom
    total_given = 100

    # Calculate the total amount spent
    total_spent = mildred_spent + candice_spent

    # Calculate the amount left with them
    amount_left = total_given - total_spent

    # Display the amount left with them
    result = amount_left
    return result

print(solution())