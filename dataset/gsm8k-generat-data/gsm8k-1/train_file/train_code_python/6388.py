def solution():
    """Central Park had 8 more than half of the number of trash cans as in Veteran's Park. Then one night, 
    someone took half of the trash cans from Central Park and put them in Veteran's Park. If originally there 
    were 24 trash cans in Veteran's Park, how many trash cans are now in Veteran's Park?"""
    
    cans_veterans_park = 24
    cans_central_park = 2*(cans_veterans_park - 8)
    
    # Half of central park cans moved to Veterans park
    cans_veterans_park += cans_central_park/2
    
    result = cans_veterans_park
    return result

print(solution())