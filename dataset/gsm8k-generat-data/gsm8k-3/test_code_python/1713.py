def solution():
    """The hobby store normally sells 21,122 trading cards per month. In June,
    the hobby store sold 3,922 more trading cards than normal. If the hobby store
    sold the regular number of trading cards in July, how many trading cards did
    the hobby store sell in June and July combined?"""
    # Define the normal number of trading cards sold per month
    NORMAL_CARDS_PER_MONTH = 21122

    # Calculate the number of trading cards sold in June
    june_cards_sold = NORMAL_CARDS_PER_MONTH + 3922

    # Calculate the total number of trading cards sold in June and July
    total_cards_sold = june_cards_sold + NORMAL_CARDS_PER_MONTH

    # Display the total number of trading cards sold
    result = total_cards_sold
    return result

print(solution())