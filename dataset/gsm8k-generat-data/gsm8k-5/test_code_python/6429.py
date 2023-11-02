def solution():
    protein_collagen = 18  # Collagen powder has 18 grams of protein for every 2 scoops
    protein_powder = 21  # Protein powder has 21 grams of protein per scoop
    protein_steak = 56  # Steak has 56 grams of protein

    # Calculate the total amount of protein Arnold will consume
    total_protein = (protein_collagen / 2) + protein_powder + protein_steak

    result = total_protein
    return result

print(solution())