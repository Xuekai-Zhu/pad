def solution():
    ticket_cost = 20  # Isabelle's ticket cost $20
    brothers_ticket_cost = 2 * 10  # Her brothers' ticket cost $10 each
    total_ticket_cost = ticket_cost + brothers_ticket_cost  # Total cost of all three tickets
    total_saved = 5 + 5  # Total amount saved by Isabelle and her brothers
    remaining_cost = total_ticket_cost - total_saved  # Amount of money needed to be earned from the job

    weeks_needed = remaining_cost / 3  # Calculate the number of weeks needed to earn the remaining amount
    result = weeks_needed
    return result

print(solution())