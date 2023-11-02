def solution():
    """Patricia is growing her long very long to donate it to a charity that makes wigs for cancer survivors. Her hair is 14 inches long. She needs to donate 23 inches to make a wig. She wants her hair to be 12 inches long after the donation. How much longer does she have to grow her hair?"""
    initial_length = 14
    wig_length = 23
    final_length = 12
    remaining_length = wig_length - final_length
    additional_length_needed = remaining_length - initial_length
    result = additional_length_needed
    return result

print(solution())