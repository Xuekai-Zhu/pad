def solution():
    # Calculate the total number of tears Trent cries
    onions = 4 * 6  # Trent needs to chop 4 onions per pot of soup and he's making 6 pots of soup.
    tears_per_onion = 2/3  # Trent cries 2 tears for every 3 onions he chops
    total_tears = onions * tears_per_onion
    result = total_tears
    return result

print(solution())