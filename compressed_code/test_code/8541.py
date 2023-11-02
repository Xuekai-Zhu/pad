def solution():
    
    photos_per_hour = 6
    price_per_photo = 15
    fuel_cost = 50 * 5
    total_photos = photos_per_hour * 5
    revenue = total_photos * price_per_photo
    profit = revenue - fuel_cost
    result = profit
    return result

print(solution())