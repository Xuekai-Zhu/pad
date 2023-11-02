def solution():
    """Patricia is growing her long very long to donate it to a charity that makes wigs for cancer survivors. Her hair is 14 inches long. She needs to donate 23 inches to make a wig. She wants her hair to be 12 inches long after the donation. How much longer does she have to grow her hair?"""
    current_length = 14
    desired_length = 12
    wig_length = 23
    length_to_donate = current_length - desired_length
    remaining_length_to_donate = wig_length - length_to_donate
    additional_length_needed = remaining_length_to_donate - current_length
    result = additional_length_needed
    return result

print(solution())