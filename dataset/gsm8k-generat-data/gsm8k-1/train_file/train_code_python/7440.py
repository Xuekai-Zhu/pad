def solution():
    """Randy drew 5 pictures. Peter drew 3 more pictures than Randy. Quincy drew 20 more pictures than Peter. How many pictures did they draw altogether?"""
    randy_pics = 5
    peter_pics = randy_pics + 3
    quincy_pics = peter_pics + 20
    total_pics = randy_pics + peter_pics + quincy_pics
    result = total_pics
    return result

print(solution())