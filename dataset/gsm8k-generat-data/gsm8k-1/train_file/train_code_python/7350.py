def solution():
    """Rita put a $120 elliptical machine on layaway at her local sports good store. After making a down payment equal to half the cost of the machine, she completely forgot about it. Sometime before the pick-up date, a store employee called offered to waive all layaway fees and taxes on the condition that Rita paid the balance within 10 days.
    What is the daily minimum amount, in dollars, that Rita must pay to own the elliptical machine?"""
    machine_cost = 120
    down_payment = machine_cost / 2
    balance = machine_cost - down_payment
    days_to_pay = 10
    daily_min_payment = balance / days_to_pay
    result = daily_min_payment
    return result

print(solution())