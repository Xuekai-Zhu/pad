def solution():
    """Isabelle gets a job so she can save enough money to go to a concert with her two brothers. Her ticket costs $20. Her brothers both get the children’s discount, and each of their tickets cost $10. Her brothers have saved $5 between the two of them and Isabelle has saved $5. If her job pays $3 per week, how many weeks must she work to afford the tickets?"""
    # Define the cost of Isabelle's ticket and her brothers' tickets
    isabelle_ticket = 20
    brothers_tickets = 2 * 10 - 5 # after their savings

    # Define the total cost of the tickets
    total_cost = isabelle_ticket + brothers_tickets

    # Define Isabelle's savings
    isabelle_savings = 5

    # Calculate the amount of money Isabelle needs to earn
    money_needed = total_cost - isabelle_savings

    # Calculate the number of weeks Isabelle needs to work
    weeks_needed = money_needed / 3

    # Return the result rounded up to the nearest integer
    result = int(weeks_needed + 0.5)
    return result

print(solution())