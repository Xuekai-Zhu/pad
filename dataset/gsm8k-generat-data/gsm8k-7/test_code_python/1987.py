def solution():
    total_cards = 120
    red_cards = total_cards * 2/5
    black_cards = (total_cards - red_cards) * 5/9
    green_cards = total_cards - red_cards - black_cards
    result = green_cards
    return result

print(solution())