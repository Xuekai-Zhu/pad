def solution():
    # Calculate the number of players who received a yellow card
    yellow_cards = 11 - 5  

    # Calculate the number of red cards that the team would collect
    red_cards = yellow_cards // 2  

    result = red_cards
    return result

print(solution())