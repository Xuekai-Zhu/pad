def solution():
    """Randy, Peter, and Quincy all drew pictures. Peter drew 8 pictures. Quincy drew 20 more pictures than Peter. If they drew 41 pictures altogether, how many did Randy draw?"""
    # Define the number of pictures drawn by Peter
    peter_pictures = 8

    # Calculate the number of pictures drawn by Quincy
    quincy_pictures = peter_pictures + 20

    # Calculate the number of pictures drawn by Randy
    randy_pictures = 41 - (peter_pictures + quincy_pictures)

    # return the result
    result = randy_pictures
    return result

print(solution())