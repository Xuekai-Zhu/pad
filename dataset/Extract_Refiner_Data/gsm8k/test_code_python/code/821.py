def solution():
    
    # Define the total number of cards and the ratio of cards between Becca, Smendrick, and PJ
    total_cards = 341
    becca_to_smendrick_ratio = 3

    # Calculate the number of cards PJ has
    pj_cards = total_cards / (1 + becca_to_smendrick_ratio + 1)

    # Calculate the number of cards Smendrick has
    smendrick_cards = pj_cards * (1 + becca_to_smendrick_ratio)

    # Calculate the number of cards Becca has
    becca_cards = smendrick_cards + 12

    # Display the number of cards Becca has
    result = becca_cards
    return result

print(solution())