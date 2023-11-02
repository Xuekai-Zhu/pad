def solution():
    """Robi and Rudy contributed money to start a business that could earn them profit. Robi contributed $4000, and Rudy contributed 1/4 more money than Robi. If they made a profit of 20 percent of the total amount and decided to share the profits equally, calculate the amount of money each got."""
    robi_contribution = 4000
    rudy_contribution = robi_contribution * 1.25
    total_contribution = robi_contribution + rudy_contribution
    profit_earned = total_contribution * 0.2
    total_money = total_contribution + profit_earned
    robi_share = total_money / 2
    rudy_share = total_money / 2
    result = (robi_share, rudy_share)
    return result

print(solution())