def solution():
    # Calculate the number of senior students who got full merit scholarships
    full_scholarships = 0.05 * 300  
    
    # Calculate the number of senior students who got half merit scholarships
    half_scholarships = 0.1 * 300  
    
    # Calculate the number of senior students who did not get any scholarships
    no_scholarships = 300 - full_scholarships - half_scholarships
    result = no_scholarships
    return result

print(solution())