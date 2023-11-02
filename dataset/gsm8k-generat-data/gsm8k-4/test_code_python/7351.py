def solution():
    """Rita put a $120 elliptical machine on layaway at her local sports good store. After making a down payment equal to half the cost of the machine, she completely forgot about it. Sometime before the pick-up date, a store employee called offered to waive all layaway fees and taxes on the condition that Rita paid the balance within 10 days. What is the daily minimum amount, in dollars, that Rita must pay to own the elliptical machine?"""
    # Define the initial cost of the elliptical machine
    machine_cost = 120

    # Calculate the remaining balance after the down payment
    remaining_balance = machine_cost / 2

    # Calculate the number of days Rita has to pay the balance
    days_to_pay = 10

    # Calculate the minimum daily payment Rita must make to fully pay off the balance
    daily_payment = remaining_balance / days_to_pay

    # Return the result
    result = daily_payment
    return result

print(solution())