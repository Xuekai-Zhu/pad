def solution():
    # Calculate the total number of pictures drawn by Peter and Quincy
    total_peter_quincy = 8 + 20  # Quincy drew 20 more pictures than Peter
    # Calculate the number of pictures drawn by Randy
    randy_pictures = 41 - total_peter_quincy
    result = randy_pictures
    return result

print(solution())