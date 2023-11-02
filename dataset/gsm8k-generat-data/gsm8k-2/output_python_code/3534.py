def solution():
    """Marcia's hair is 24" long at the beginning of the school year. She cuts half of her hair off and lets it grow out 4 more inches. She then cuts off another 2" of hair. How long is her hair?"""
    initial_hair_length = 24
    half_hair_length = initial_hair_length / 2
    grown_hair_length = half_hair_length + 4
    final_hair_length = grown_hair_length - 2
    result = final_hair_length
    return result

print(solution())