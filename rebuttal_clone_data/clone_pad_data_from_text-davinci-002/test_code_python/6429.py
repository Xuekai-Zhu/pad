def solution():
     scoop_collagen = 2
     protein_collagen = 18
     scoop_protein = 1
     protein_protein = 21
     steak_protein = 56
     total_protein = (scoop_collagen / 2) * protein_collagen + scoop_protein * protein_protein + steak_protein
     result = total_protein
     return result

print(solution())