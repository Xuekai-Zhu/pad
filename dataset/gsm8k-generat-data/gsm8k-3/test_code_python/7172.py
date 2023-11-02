def solution():
    """Every time Carl earned $0.50 he would go to the corner market and buy a candy bar.  Carl's neighbor said he would pay him $0.75 every week for taking out his trash.  At the end of four weeks, how many candy bars will Carl be able to buy?"""
    # Define the amount earned per candy bar and the weekly payment
    CANDY_PRICE = 0.5
    WEEKLY_PAYMENT = 0.75

    # Calculate the total amount earned from selling candy bars
    candy_earnings = 4 * (WEEKLY_PAYMENT / CANDY_PRICE)

    # Display the number of candy bars Carl can buy
    result = candy_earnings
    return result

print(solution())