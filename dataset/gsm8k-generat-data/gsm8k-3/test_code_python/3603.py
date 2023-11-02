def solution():
    """Robi and Rudy contributed money to start a business that could earn them profit. Robi contributed $4000, and Rudy contributed 1/4 more money than Robi. If they made a profit of 20 percent of the total amount and decided to share the profits equally, calculate the amount of money each got."""
    
    # Robi's contribution
    robis_contribution = 4000

    # Rudy's contribution
    rudy_contribution = robis_contribution * (1 + 1/4)

    # Total amount contributed
    total_contributed = robis_contribution + rudy_contribution

    # Profit earned
    profit = total_contributed * 0.2

    # Amount each person gets
    each_gets = profit / 2

    result = each_gets
    return result

print(solution())