def solution():
    """Trent cries 2 tears for every three onions he chops. He needs to chop 4 onions per pot of soup. If he's making 6 pots of soup, how many tears does he cry?"""
    # Define the tear-to-onion ratio
    TEAR_ONION_RATIO = 2/3

    # Define the number of onions per pot of soup
    ONIONS_PER_POT = 4

    # Define the number of pots of soup
    POTS_OF_SOUP = 6

    # Calculate the total number of onions Trent needs to chop
    total_onions = ONIONS_PER_POT * POTS_OF_SOUP

    # Calculate the total number of tears Trent will cry
    total_tears = total_onions * TEAR_ONION_RATIO

    # Display the total number of tears
    result = total_tears
    return result

print(solution())