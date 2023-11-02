def solution():
    # Define the variables
    starting_cards = 0
    new_cards = 8
    remaining_cards = 46

    # Find the total number of cards before the dog ate them
    total_cards = remaining_cards * 2

    # Subtract the new cards from the total to find the starting number
    starting_cards = total_cards - new_cards
    result = starting_cards
    return result

print(solution())