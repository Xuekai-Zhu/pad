def solution():
    
    weight = 80  
    protein_per_day = 2  
    protein_ratio = 0.8
    total_protein_per_day = weight * protein_per_day
    protein_needed = total_protein_per_day / protein_ratio
    protein_per_week = protein_needed * 7
    result = protein_per_week
    return result

print(solution())