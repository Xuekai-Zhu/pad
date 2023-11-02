def solution():
    """Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38. How old was Teresa when she gave birth to Michiko?"""
    # Calculate the age gap between Morio and Michiko
    age_gap = 71 - 38
    # Teresa's age when Michiko was born = Teresa's current age - age gap
    teresa_age_at_birth = 59 - age_gap
    
    result = teresa_age_at_birth
    return result

print(solution())