def solution():
    """Patricia is growing her long very long to donate it to a charity that makes wigs for cancer survivors. Her hair is 14 inches long. 
    She needs to donate 23 inches to make a wig. She wants her hair to be 12 inches long after the donation. 
    How much longer does she have to grow her hair?"""
    # Define Patricia's current hair length and desired length after donation
    current_length = 14
    desired_length = 12

    # Define the length needed for the wig
    wig_length = 23

    # Calculate the length Patricia needs to grow her hair
    length_needed = wig_length - (current_length - desired_length)

    # Display the length Patricia needs to grow her hair
    result = length_needed
    return result

print(solution())