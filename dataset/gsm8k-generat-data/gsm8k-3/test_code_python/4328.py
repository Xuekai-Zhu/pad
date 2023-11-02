def solution():
    """The fisherman gets 8 Red snappers and 14 Tunas every day. If a Red snapper costs $3 and a Tuna costs $2, how much does he earn every day?"""
    # Define the price of each type of fish
    RED_SNAPPER_PRICE = 3
    TUNA_PRICE = 2

    # Define the number of each type of fish caught per day
    red_snappers = 8
    tunas = 14

    # Calculate the total earnings per day
    total_earnings = (red_snappers * RED_SNAPPER_PRICE) + (tunas * TUNA_PRICE)

    # Display the total earnings
    result = total_earnings
    return result

print(solution())