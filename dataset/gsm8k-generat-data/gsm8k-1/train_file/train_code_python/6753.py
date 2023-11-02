def solution():
    """Randy, Peter, and Quincy all drew pictures. Peter drew 8 pictures. Quincy drew 20 more pictures than Peter. If they drew 41 pictures altogether, how many did Randy draw?"""
    peter_pictures = 8
    quincy_pictures = peter_pictures + 20
    total_pictures = 41
    randy_pictures = total_pictures - (peter_pictures + quincy_pictures)
    result = randy_pictures
    return result

print(solution())