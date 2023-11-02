def solution():
    """Robi and Rudy contributed money to start a business that could earn them profit. Robi contributed $4000, and Rudy contributed 1/4 more money than Robi. If they made a profit of 20 percent of the total amount and decided to share the profits equally, calculate the amount of money each got."""
    # Define the amount contributed by Robi
    robis_contribution = 4000

    # Calculate the amount contributed by Rudy
    rudys_contribution = robis_contribution * (1 + 1/4)

    # Calculate the total amount contributed
    total_contribution = robis_contribution + rudys_contribution

    # Calculate the total profit made
    total_profit = total_contribution * 0.2

    # Calculate the profit each person gets
    profit_per_person = total_profit / 2

    # Calculate the amount of money each person gets
    robi_share = robis_contribution + profit_per_person
    rudy_share = rudys_contribution + profit_per_person

    # Return the result
    result = (robi_share, rudy_share)
    return result

print(solution())