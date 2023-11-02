def solution():
    
    photo_value = 15
    shark_frequency = 1 / 10 
    total_minutes = 5 * 60 
    total_sharks = shark_frequency * total_minutes
    total_photos = total_sharks
    total_earnings = total_photos * photo_value
    fuel_cost = 50 * 5 
    profit = total_earnings - fuel_cost
    result = profit
    return result

print(solution())