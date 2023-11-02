def solution():
    """A family went out to see a movie. The regular ticket costs $9 and the ticket for children is $2 less. They gave the cashier two $20 bills and they received a $1 change. How many children are there if there are 2 adults in the family?"""
    adult_tickets = 2
    adult_cost = 9
    child_cost = adult_cost - 2
    total_cost = (adult_tickets * adult_cost) + (child_tickets * child_cost)
    amount_paid = (20 * 2) + 1
    change = amount_paid - total_cost
    child_tickets = (change // child_cost)
    result = child_tickets
    
    return result

print(solution())