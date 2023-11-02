def solution():
    """Thor is 13 times older than Captain America. Captain America is 7 times older than Peter Parker, and Ironman is 32 years older than Peter Parker. How old is Ironman if Thor is 1456 years old?"""
    # Given that Thor is 1456 years old
    thor_age = 1456
    
    # Calculate Captain America's age
    cap_age = thor_age / 13
    
    # Calculate Peter Parker's age
    pp_age = cap_age / 7
    
    # Calculate Ironman's age
    im_age = pp_age + 32
    
    # Return Ironman's age
    result = im_age
    return result

print(solution())