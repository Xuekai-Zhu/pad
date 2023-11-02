def solution():
    """Marcia's hair is 24" long at the beginning of the school year. She cuts half of her hair off and lets it grow out 4 more inches. She then cuts off another 2" of hair. How long is her hair?"""
    # Start with 24" of hair
    hair_length = 24

    # Cut off half of her hair and let it grow 4 more inches
    hair_length = (hair_length / 2) + 4

    # Cut off another 2" of hair
    hair_length -= 2

    # Display the final length of her hair
    result = hair_length
    return result

print(solution())