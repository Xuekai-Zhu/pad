def solution():
    """A couple with two children, ages 6 and 10 years old, decided to go to an amusement park. The regular ticket costs $109, but children below 12 years old have a $5 discount. If they gave the cashier $500, how much change will they receive?"""
    regular_ticket_cost = 109
    child_ticket_discount = 5
    total_ticket_cost = regular_ticket_cost - (child_ticket_discount * 2)
    cash_given = 500
    cash_returned = cash_given - total_ticket_cost
    result = cash_returned
    return result

print(solution())