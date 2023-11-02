def solution():
    thursday_practice = 50
    
    wednesday_practice = thursday_practice + 5
    
    tuesday_practice = wednesday_practice - 10
    
    monday_practice = tuesday_practice * 2
    
    total_practice = thursday_practice + wednesday_practice + tuesday_practice + monday_practice
    
    minutes_remaining = (5*60) - total_practice
    
    friday_practice = minutes_remaining / 60
    
    result = friday_practice
    
    return result

print(solution())