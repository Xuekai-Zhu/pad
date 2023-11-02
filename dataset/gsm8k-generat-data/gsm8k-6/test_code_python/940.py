def solution():
    # Calculate the current number of cards for Mark and Lloyd
    cards_Mark = 100 - 10  # Mark has 10 fewer cards than Michael
    cards_Lloyd = cards_Mark // 3  # Mark has thrice as many cards as Lloyd

    # Find the number of cards they need to collect to have a total of 300 cards
    total_cards_needed = 300 - (cards_Mark + cards_Lloyd + 100)
    result = total_cards_needed
    return result

print(solution())