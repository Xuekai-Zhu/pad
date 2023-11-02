def solution():
    """Robi and Rudy contributed money to start a business that could earn them profit.
    Robi contributed $4000, and Rudy contributed 1/4 more money than Robi.
    If they made a profit of 20 percent of the total amount and decided to share the profits equally,
    calculate the amount of money each got."""
    robi_contributed = 4000
    rudy_contributed = robi_contributed * 1.25
    total_money = robi_contributed + rudy_contributed
    profit = total_money * 0.2
    total_money_with_profit = total_money + profit
    each_gets = total_money_with_profit / 2
    result = each_gets
    return result

print(solution())