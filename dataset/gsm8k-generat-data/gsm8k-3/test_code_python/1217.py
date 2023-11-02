def solution():
    """Camden just bought 3/4 times as many dogs as Rico, who has 10 more dogs than Justin. If Justin has 14 dogs,
    what's the total number of legs that Camden's dogs have?"""
    # Determine the number of dogs that Justin has
    justin_dogs = 14
    
    # Determine the number of dogs that Rico has
    rico_dogs = justin_dogs + 10
    
    # Determine the number of dogs that Camden has
    camden_dogs = (3/4) * rico_dogs
    
    # Determine the total number of legs that Camden's dogs have
    total_legs = camden_dogs * 4
    
    # Display the total number of legs
    result = total_legs
    return result

print(solution())