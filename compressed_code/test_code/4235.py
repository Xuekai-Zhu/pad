def solution():
    
    cement_bags = 500
    cement_price = 10
    sand_lorries = 20
    sand_price = 40
    sand_tons = sand_lorries * 10
    total_cement_price = cement_bags * cement_price
    total_sand_price = sand_tons * sand_price
    total_price = total_cement_price + total_sand_price
    result = total_price
    return result

print(solution())