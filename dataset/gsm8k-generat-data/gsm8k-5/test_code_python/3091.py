def solution():
    sodas_before = 22  # Marcy had 22 sodas before her friend Tina came over
    sodas_from_tina = 12 + 2*sodas_before  # Tina gave Marcy 12 sodas plus 2 times the number of sodas Marcy had before
    total_sodas = sodas_before + sodas_from_tina  # Calculate the total number of sodas Marcy will have for the party
    result = total_sodas
    return result

print(solution())