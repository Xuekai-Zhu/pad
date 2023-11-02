def solution():
    # Find the number of guppies Haylee has
    haylee = 3 * 12
    
    # Find the number of guppies Jose has
    jose = haylee / 2
    
    # Find the number of guppies Charliz has
    charliz = jose / 3
    
    # Find the number of guppies Nicolai has
    nicolai = charliz * 4
    
    # Find the total number of guppies
    total_guppies = haylee + jose + charliz + nicolai
    result = total_guppies
    return result

print(solution())