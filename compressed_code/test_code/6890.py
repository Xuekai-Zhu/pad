def solution():
    
    
    boys_attended = 16
    girls_attended = 14
    
    
    boys_with_gifts = (3/4) * boys_attended
    girls_with_gifts = (6/7) * girls_attended
    
    
    total_with_gifts = boys_with_gifts + girls_with_gifts
    
    
    total_attended = boys_attended + girls_attended
    without_gifts = total_attended - total_with_gifts
    
    result = without_gifts
    return result

print(solution())