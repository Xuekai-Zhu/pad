def solution():
    # Let x be the length of the short side of the fence
    x = 0.0
    
    # The long sides are three times the length of the short sides
    y = 3 * x
    
    # The perimeter of the fence is 640 feet
    perimeter = x + y + x + y
    
    # One short side needs to be replaced, so we subtract its length from the perimeter
    new_perimeter = perimeter - x
    
    # The length of the new fence needed is the difference in perimeters
    fence_length = perimeter - new_perimeter
    
    result = fence_length
    return result

print(solution())