def solution():
    """Patricia is growing her long very long to donate it to a charity that makes wigs for cancer survivors. Her hair is 14 inches long. She needs to donate 23 inches to make a wig. She wants her hair to be 12 inches long after the donation. How much longer does she have to grow her hair?"""
    # Define the initial length of Patricia's hair
    initial_length = 14

    # Define the desired length of Patricia's hair after donation
    desired_length = 12

    # Define the length of hair needed to make a wig
    wig_length = 23

    # Calculate the remaining length of hair needed to make a wig
    remaining_length = wig_length - desired_length

    # Calculate how much longer Patricia needs to grow her hair
    additional_length = remaining_length - initial_length

    # Display the result
    result = additional_length
    return result

print(solution())