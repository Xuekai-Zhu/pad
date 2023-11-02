def solution():
    """Trevor and two of his neighborhood friends go to the toy shop every year to buy toys. Trevor always spends $20 more than his friend Reed on toys, and Reed spends 2 times as much money as their friend Quinn on the toys. If Trevor spends $80 every year to buy his toys, calculate how much money in total the three spend in 4 years."""
    # Calculate the amount Reed spends on toys each year
    reed_spending = 80 - 20
    # Calculate the amount Quinn spends on toys each year
    quinn_spending = reed_spending / 2
    # Calculate the total amount spent by the three friends on toys each year
    total_spending = 80 + reed_spending + quinn_spending
    # Calculate the total amount spent by the three friends on toys over 4 years
    total_spending_4_years = total_spending * 4
    result = total_spending_4_years
    return result

print(solution())