def solution():
    """Arnold's collagen powder has 18 grams of protein for every 2 scoops. His protein powder has 21 grams of protein per scoop. And his steak has 56 grams of protein. If he has 1 scoop of collagen powder, 1 scoop of protein powder and his steak, how many grams of protein will he consume?"""
    collagen_protein_ratio = 18 / 2
    collagen_scoops = 1
    collagen_protein = collagen_scoops * collagen_protein_ratio
    protein_scoops = 1
    protein_protein_ratio = 21
    protein_protein = protein_scoops * protein_protein_ratio
    steak_protein = 56
    
    total_protein = collagen_protein + protein_protein + steak_protein
    result = total_protein
    
    return result

print(solution())