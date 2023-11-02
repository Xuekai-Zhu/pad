def solution():
    
    
    
    boys_in_class = 10
    girls_in_class = 2 * boys_in_class
    
    
    cups_per_boy = 5
    total_cups_by_boys = cups_per_boy * boys_in_class
    
    
    total_cups = 90
    total_cups_by_girls = total_cups - total_cups_by_boys
    
    
    cups_per_girl = total_cups_by_girls / girls_in_class
    
    result = cups_per_girl
    return result

print(solution())