def solution():
    """Matt's protein powder is 80% protein. He weighs 80 kg and wants to eat 2 grams of protein per kilogram of body weight each day. How much protein powder does he need to eat per week?"""
    protein_percent = 80
    weight = 80
    protein_per_day = 2 * weight
    protein_per_week = protein_per_day * 7
    protein_availability = protein_percent / 100
    protein_needed = protein_per_day / protein_availability
    powder_needed = protein_needed / 1000
    result = powder_needed * 7
    
    return result

print(solution())