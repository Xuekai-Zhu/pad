def solution():
    """Arnold's collagen powder has 18 grams of protein for every 2 scoops.  His protein powder has 21 grams of protein per scoop.  And his steak has 56 grams of protein.   If he has 1 scoop of collagen powder, 1 scoop of protein powder and his steak, how many grams of protein will he consume?"""
    # Calculate the total grams of protein from the collagen powder
    collagen_protein = 18/2

    # Calculate the total grams of protein from the protein powder
    protein_powder_protein = 21

    # Calculate the total grams of protein from the steak
    steak_protein = 56

    # Calculate the total grams of protein consumed
    total_protein = collagen_protein + protein_powder_protein + steak_protein

    # Display the total grams of protein consumed
    result = total_protein
    return result

print(solution())