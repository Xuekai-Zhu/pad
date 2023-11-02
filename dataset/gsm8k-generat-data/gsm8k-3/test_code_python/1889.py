def solution():
    """Trevor and two of his neighborhood friends go to the toy shop every year to buy toys. Trevor always spends $20 more than his
    friend Reed on toys, and Reed spends 2 times as much money as their friend Quinn on the toys. If Trevor spends $80 every
    year to buy his toys, calculate how much money in total the three spend in 4 years."""
    # Define the amount Trevor spends on toys
    trevor_spending = 80

    # Calculate Reed's spending based on Trevor's spending
    reed_spending = trevor_spending - 20

    # Calculate Quinn's spending based on Reed's spending
    quinn_spending = reed_spending / 2

    # Calculate the total spending of the three friends for one year
    total_spending = trevor_spending + reed_spending + quinn_spending

    # Calculate the total spending of the three friends for four years
    total_spending_4_years = total_spending * 4

    # Display the total spending for four years
    result = total_spending_4_years
    return result

print(solution())