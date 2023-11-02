def solution():
    """A couple with two children, ages 6 and 10 years old, decided to go to an amusement park. The regular ticket costs $109, but children below 12 years old have a $5 discount. If they gave the cashier $500, how much change will they receive?"""
    adult_ticket_cost = 109
    child_ticket_cost = adult_ticket_cost - 5
    num_adults = 2
    num_children = 2
    total_cost = (adult_ticket_cost * num_adults) + (child_ticket_cost * num_children)
    amount_paid = 500
    change = amount_paid - total_cost
    result = change
    return result

print(solution())