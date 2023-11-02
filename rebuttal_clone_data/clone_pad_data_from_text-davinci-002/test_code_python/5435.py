def solution():
    percent_protein = 80
    weight_in_kg = 80
    daily_protein_goal = 2
    powder_to_protein_ratio = percent_protein / 100
    protein_needed = weight_in_kg * daily_protein_goal
    powder_needed = protein_needed / powder_to_protein_ratio

print(solution())