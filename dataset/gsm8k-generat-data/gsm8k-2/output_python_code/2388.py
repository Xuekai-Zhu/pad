def solution():
    """Marcus takes a deck of standard playing cards and takes out all the face cards and the 8's. Mark picks a card at random and then replaces it 36 times. How many times should he expect to pick a card that's both red and has a number divisible by 3?"""
    total_cards = 36
    red_cards = 26
    divisible_by_3 = 8  # There are 4 cards with a number divisible by 3 in each suit
    red_and_divisible_by_3 = 4  # There are 2 red cards with a number divisible by 3 in each suit
    
    probability_red = red_cards / total_cards
    probability_divisible_by_3 = divisible_by_3 / total_cards
    probability_red_and_divisible_by_3 = (red_and_divisible_by_3 * 2) / total_cards  # Multiply by 2 since there are 2 suits that satisfy the condition
    
    expected_frequency = probability_red * probability_divisible_by_3 * total_cards
    expected_red_and_divisible_by_3 = probability_red_and_divisible_by_3 * total_cards
    
    result = expected_red_and_divisible_by_3
    return result

print(solution())