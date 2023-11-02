def solution():
    # Define the cost of Isabelle's ticket and her brothers' tickets
    isabelle_ticket_cost = 20
    brothers_ticket_cost = 2 * 10

    # Define the total cost of the tickets
    total_ticket_cost = isabelle_ticket_cost + brothers_ticket_cost

    # Define the total amount saved by Isabelle and her brothers
    total_saved = 5 + 5

    # Calculate the amount of money Isabelle still needs to save
    amount_to_save = total_ticket_cost - total_saved

    # Calculate the number of weeks Isabelle needs to work to save the remaining amount
    weeks_to_work = amount_to_save / 3
    result = weeks_to_work
    return result

print(solution())