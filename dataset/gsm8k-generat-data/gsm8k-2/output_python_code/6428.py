def solution():
    """Arnold's collagen powder has 18 grams of protein for every 2 scoops. His protein powder has 21 grams of protein per scoop. And his steak has 56 grams of protein. If he has 1 scoop of collagen powder, 1 scoop of protein powder and his steak, how many grams of protein will he consume?"""
    collagen_scoops = 1
    protein_scoops = 1
    steak_protein = 56
    collagen_protein = collagen_scoops * (18/2)
    protein_protein = protein_scoops * 21
    total_protein = collagen_protein + protein_protein + steak_protein
    result = total_protein
    return result

print(solution())