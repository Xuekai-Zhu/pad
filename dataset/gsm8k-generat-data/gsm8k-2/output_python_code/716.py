def solution():
    """Jake splits 8 shots of vodka with his friend. Each shot of vodka is 1.5 ounces. If the vodka is 50% pure alcohol, how much pure alcohol did Jake drink?"""
    num_shots = 8
    shot_size = 1.5 #ounces
    alcohol_percent = 50 #%
    alcohol_per_shot = shot_size * (alcohol_percent/100)
    total_alcohol = num_shots * alcohol_per_shot
    result = total_alcohol
    return result

print(solution())