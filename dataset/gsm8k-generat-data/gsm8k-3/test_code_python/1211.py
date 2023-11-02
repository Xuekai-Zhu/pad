def solution():
    """Isabelle gets a job so she can save enough money to go to a concert with her two brothers. Her ticket costs $20. 
    Her brothers both get the children’s discount, and each of their tickets cost $10. Her brothers have saved $5 between 
    the two of them and Isabelle has saved $5. If her job pays $3 per week, how many weeks must she work to afford the tickets?"""
    
    # Define the cost of Isabelle's ticket and her brothers' tickets
    isabelle_ticket_cost = 20
    brothers_ticket_cost = 10
    
    # Calculate the total cost of the tickets
    total_cost = isabelle_ticket_cost + (2 * brothers_ticket_cost) - 10
    
    # Calculate the amount of money Isabelle needs to save
    isabelle_savings_needed = total_cost - 5
    
    # Calculate the number of weeks Isabelle needs to work
    weeks_needed = isabelle_savings_needed / 3
    
    # Round up to the nearest whole number of weeks
    weeks_needed = math.ceil(weeks_needed)
    
    result = weeks_needed
    return result

print(solution())