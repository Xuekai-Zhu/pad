def solution():
    """Randy, Peter, and Quincy all drew pictures. Peter drew 8 pictures. Quincy drew 20 more pictures than Peter. If they drew 41 pictures altogether, how many did Randy draw?"""
    # Define the number of pictures Peter drew
    peter_pictures = 8

    # Define the number of pictures Quincy drew
    quincy_pictures = peter_pictures + 20

    # Calculate the number of pictures Randy drew
    randy_pictures = 41 - peter_pictures - quincy_pictures

    # Display the number of pictures Randy drew
    result = randy_pictures
    return result

print(solution())