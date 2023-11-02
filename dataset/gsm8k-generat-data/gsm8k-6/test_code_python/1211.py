def solution():
    # Calculate the total cost of the tickets
    total_cost = 20 + 2*10 - 5  # The total cost is $20 for Isabelle's ticket and $10 each for her brothers' tickets, minus the $5 they have already saved

    # Calculate the amount of money Isabelle still needs to save
    money_left = total_cost - 5 - 5  # Isabelle and her brothers have already saved a total of $10

    # Calculate the number of weeks Isabelle needs to work to save enough money
    weeks_needed = money_left / 3  # Isabelle earns $3 per week

    result = weeks_needed
    return result

print(solution())