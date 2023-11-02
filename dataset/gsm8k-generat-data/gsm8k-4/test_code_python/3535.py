def solution():
    """Marcia's hair is 24" long at the beginning of the school year. She cuts half of her hair off and lets it grow out 4 more inches. She then cuts off another 2" of hair. How long is her hair?"""
    # Define the initial length of Marcia's hair
    initial_length = 24

    # Calculate the length after cutting half of it off
    length_after_cutting = initial_length / 2

    # Calculate the length after letting it grow out 4 more inches
    length_after_growing = length_after_cutting + 4

    # Calculate the length after cutting off another 2 inches
    final_length = length_after_growing - 2

    result = final_length
    return result

print(solution())