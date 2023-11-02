def solution():
    """Trent cries 2 tears for every three onions he chops. He needs to chop 4 onions per pot of soup. If he's making 6 pots of soup, how many tears does he cry?"""
    # Define the tears-to-onion ratio
    tears_per_onion = 2 / 3

    # Define the number of onions Trent needs to chop for each pot of soup
    onions_per_pot = 4

    # Define the total number of pots of soup Trent is making
    total_pots = 6

    # Calculate the total number of onions Trent needs to chop
    total_onions = onions_per_pot * total_pots

    # Calculate the total number of tears Trent will cry
    total_tears = total_onions * tears_per_onion

    result = total_tears
    return result

print(solution())