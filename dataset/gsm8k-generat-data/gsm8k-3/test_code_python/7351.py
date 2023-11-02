def solution():
    """Rita put a $120 elliptical machine on layaway at her local sports good store. After making a down payment equal to half the cost of the machine, she completely forgot about it. Sometime before the pick-up date, a store employee called offered to waive all layaway fees and taxes on the condition that Rita paid the balance within 10 days. What is the daily minimum amount, in dollars, that Rita must pay to own the elliptical machine?"""
    # Define the cost of the elliptical machine
    MACHINE_COST = 120

    # Calculate the amount of the down payment
    down_payment = MACHINE_COST / 2

    # Calculate the remaining balance
    remaining_balance = MACHINE_COST - down_payment

    # Calculate the minimum daily payment needed to pay off the balance within 10 days
    daily_payment = remaining_balance / 10

    # Display the minimum daily payment
    result = daily_payment
    return result

print(solution())