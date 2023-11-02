def solution():
    # Calculate how many cards Padma has after trading
    padma_cards = 75 - 2 + 10

    # Calculate how many cards Robert has after trading
    robert_cards = 88 - 8 + 15

    # Calculate the total number of cards traded
    total_traded = (75 + 10 + 15 + 88) - (padma_cards + robert_cards)

    result = total_traded
    return result

print(solution())