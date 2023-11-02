def solution():
    collagen_protein_per_scoop = 18 / 2  # 9 grams of protein per scoop
    protein_powder_protein_per_scoop = 21
    steak_protein = 56

    # Calculate the total grams of protein Arnold will consume
    total_protein = collagen_protein_per_scoop + protein_powder_protein_per_scoop + steak_protein
    result = total_protein
    return result

print(solution())