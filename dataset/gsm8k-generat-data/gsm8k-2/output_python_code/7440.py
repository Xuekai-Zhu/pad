def solution():
    """Randy drew 5 pictures. Peter drew 3 more pictures than Randy. Quincy drew 20 more pictures than Peter. How many pictures did they draw altogether?"""
    randy_pictures = 5
    peter_pictures = randy_pictures + 3
    quincy_pictures = peter_pictures + 20
    total_pictures = randy_pictures + peter_pictures + quincy_pictures
    result = total_pictures
    return result

print(solution())