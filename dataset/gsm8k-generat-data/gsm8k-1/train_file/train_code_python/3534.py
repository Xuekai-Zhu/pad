def solution():
    """Marcia's hair is 24" long at the beginning of the school year. She cuts half of her hair off and lets it grow out 4 more inches. She then cuts off another 2" of hair. How long is her hair?"""
    initial_length = 24
    cut_length = initial_length / 2
    regrowth_length = 4
    first_length = initial_length - cut_length + regrowth_length
    second_length = first_length - 2
    result = second_length
    return result

print(solution())