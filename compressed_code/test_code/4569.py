def solution():
    
    total_spots = 59
    
    x = 0
    
    
    bill_spots = 2*x - 1
    
    
    x = (total_spots + 1) / 3
    
    bill_spots = 2*x - 1
    result = bill_spots
    return result

print(solution())