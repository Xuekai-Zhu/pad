def solution():
    """Sixteen boys and 14 girls attended Simon's birthday party. 
    Three-fourths of the boys and 6/7 of the girls brought gifts. 
    How many of those who attended did not bring gifts?"""
    
    boys_attended = 16
    girls_attended = 14
    
    # number of boys and girls who brought gifts
    boys_with_gifts = (3/4) * boys_attended
    girls_with_gifts = (6/7) * girls_attended
    
    # total number of people with gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts
    
    # number of people without gifts
    total_attended = boys_attended + girls_attended
    without_gifts = total_attended - total_with_gifts
    
    result = without_gifts
    return result

print(solution())