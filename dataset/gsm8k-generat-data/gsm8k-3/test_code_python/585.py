def solution():
    """Maddy's 4th grade class needs to make 1000 Valentine's Day cards to get a pizza party. There are 30 kids in the class. If everyone makes 8, how many more cards will they need to make to get a pizza party?"""
    # Calculate the total number of cards the class can make
    total_cards = 30 * 8

    # Calculate the remaining number of cards needed for the pizza party
    remaining_cards = 1000 - total_cards

    # Display the number of cards needed
    result = remaining_cards
    return result

print(solution())