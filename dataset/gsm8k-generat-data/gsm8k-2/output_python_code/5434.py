def solution():
    """Matt's protein powder is 80% protein. He weighs 80 kg and wants to eat 2 grams of protein per kilogram of body weight each day. How much protein powder does he need to eat per week?"""
    weight = 80  # kilograms
    protein_per_day = 2  # grams/kg
    protein_ratio = 0.8
    total_protein_per_day = weight * protein_per_day
    protein_needed = total_protein_per_day / protein_ratio
    protein_per_week = protein_needed * 7
    result = protein_per_week
    return result

print(solution())