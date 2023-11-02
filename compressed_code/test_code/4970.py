def solution():
    
    collagen_scoops = 1
    protein_scoops = 1
    steak_protein = 56
    collagen_protein = collagen_scoops * (18/2)
    protein_protein = protein_scoops * 21
    total_protein = collagen_protein + protein_protein + steak_protein
    result = total_protein
    return result

print(solution())