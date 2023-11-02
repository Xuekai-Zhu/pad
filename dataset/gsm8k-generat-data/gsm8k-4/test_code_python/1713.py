def solution():
    """The hobby store normally sells 21,122 trading cards per month. In June, the hobby store sold 3,922 more trading cards than normal. If the hobby store sold the regular number of trading cards in July, how many trading cards did the hobby store sell in June and July combined?"""
    # Define the normal number of trading cards sold per month and the number of extra cards sold in June
    normal_cards_per_month = 21122
    extra_cards_in_june = 3922

    # Calculate the total number of cards sold in June and July combined
    total_cards = normal_cards_per_month + extra_cards_in_june + normal_cards_per_month

    # return the result
    result = total_cards
    return result

print(solution())