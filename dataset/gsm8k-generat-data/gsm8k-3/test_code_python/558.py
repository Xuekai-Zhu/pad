def solution():
    """Jack is on the phone with a scammer who says the IRS will arrest Jack if he doesn't send them the codes from 6 $500 Best Buy gift cards and 9 $200 Walmart gift cards. After sending the codes for 1 Best Buy gift card and 2 Walmart gift cards, Jack wises up and hangs up. How many dollars' worth of gift cards can he still return?"""
    # Define the value of each gift card
    BEST_BUY_VALUE = 500
    WALMART_VALUE = 200

    # Define the number of gift cards
    num_best_buy = 6
    num_walmart = 9

    # Calculate the total value of the gift cards
    total_value = (num_best_buy * BEST_BUY_VALUE) + (num_walmart * WALMART_VALUE)

    # Calculate the value of the gift cards that Jack has already given away
    given_away_value = (1 * BEST_BUY_VALUE) + (2 * WALMART_VALUE)

    # Calculate the value of the gift cards that Jack can still return
    return_value = total_value - given_away_value

    # Display the value of the gift cards that Jack can still return
    result = return_value
    return result

print(solution())