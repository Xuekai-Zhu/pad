def solution():
    jimmy_cards = 18
    bob_cards = 3
    mary_cards = bob_cards * 2

    # Calculate the total number of cards given away
    total_given = bob_cards + mary_cards

    # Subtract the total given from Jimmy's original cards to get the remaining cards
    remaining_cards = jimmy_cards - total_given
    result = remaining_cards
    return result

print(solution())