def solution():
    
    total_potatoes = 6500
    damaged_potatoes = 150
    sellable_potatoes = total_potatoes - damaged_potatoes
    bag_size = 50
    bags_available = sellable_potatoes // bag_size
    bag_price = 72
    total_price = bags_available * bag_price
    result = total_price
    return result

print(solution())