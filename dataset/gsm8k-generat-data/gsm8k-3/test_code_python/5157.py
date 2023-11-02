def solution():
    """Jason waits on a customer whose check comes to $15.00. Jason's state applies a 20% tax to restaurant sales. If the customer gives Jason a $20 bill and tells him to keep the change, how much is Jason's tip?"""
    # Define the tax rate
    TAX_RATE = 0.2

    # Calculate the total cost of the meal with tax
    total_cost = 15 + (15 * TAX_RATE)

    # Calculate the amount of change Jason should give to the customer
    change = 20 - total_cost

    # The amount of the tip is the change
    tip = change

    # Display the amount of the tip
    result = tip
    return result

print(solution())