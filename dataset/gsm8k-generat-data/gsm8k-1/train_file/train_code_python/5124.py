def solution():
    """Jonathan ran 7.5 kilometers. Mercedes ran twice that distance and Davonte ran 2 kilometers farther than Mercedes. How many kilometers did Mercedes and Davonte run in total?"""
    
    jonathan_distance = 7.5
    mercedes_distance = jonathan_distance * 2
    davonte_distance = mercedes_distance + 2
    
    total_distance = mercedes_distance + davonte_distance
    
    result = total_distance
    
    return result

print(solution())