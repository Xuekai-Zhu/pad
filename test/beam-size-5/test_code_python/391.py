def solution():
    
    # Define the initial number of Valentine's cards
    initial_cards = 20

    # Define the number of boxes of Valentine's cards
    boxes = 2

    # Define the number of pre-made Valentine's cards
    pre_made_cards = 15 * boxes

    # Define the number of cards passed out to classmates
    classmates_cards = 24

    # Define the number of cards passed out to family
    family_cards = 5

    # Define the number of cards received from family and friends
    friends_cards = 17

    # Calculate the total number of cards
    total_cards = initial_cards + classmates_cards + family_cards + friends_cards

    # Display the total number of cards
    result = total_cards
    return result

print(solution())