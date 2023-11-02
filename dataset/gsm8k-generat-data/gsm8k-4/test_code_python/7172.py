def solution():
    """Every time Carl earned $0.50 he would go to the corner market and buy a candy bar.  Carl's neighbor said he would pay him $0.75 every week for taking out his trash.  At the end of four weeks, how many candy bars will Carl be able to buy?"""
    # Define the cost of a candy bar and the weekly payment from Carl's neighbor
    CANDY_BAR_COST = 0.5
    WEEKLY_PAYMENT = 0.75

    # Initialize the total earnings and the number of candy bars bought with it
    total_earnings = 0
    candy_bars_bought = 0

    # Calculate the total earnings after 4 weeks
    for i in range(4):
        total_earnings += 0.5
        total_earnings += WEEKLY_PAYMENT

    # Calculate the number of candy bars that can be bought with the total earnings
    candy_bars_bought = total_earnings // CANDY_BAR_COST

    # Return the result
    result = int(candy_bars_bought)
    return result

print(solution())