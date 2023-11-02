def solution():
    """Tayzia and her two young daughters get haircuts.  Women's haircuts are $48.  Children's haircuts are $36.  If Tayzia wants to give a 20% tip to the hair stylist, how much would it be?"""
    # Define the prices for women's and children's haircuts
    WOMEN_PRICE = 48
    CHILD_PRICE = 36

    # Define the number of each type of haircut received
    women_haircuts = 1
    child_haircuts = 2

    # Calculate the total cost for all three haircuts
    total_cost = (women_haircuts * WOMEN_PRICE) + (child_haircuts * CHILD_PRICE)

    # Calculate the 20% tip
    tip_amount = 0.2 * total_cost

    # Calculate the total cost including the tip
    total_cost_with_tip = total_cost + tip_amount

    # Display the total cost with tip
    result = total_cost_with_tip
    return result

print(solution())