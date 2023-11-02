def solution():
    
    total_milliliters = 0
    liters = 0
    milliliters = 0
    volumes = [2000, 750, 250]

    for volume in volumes:
        total_milliliters += volume

    liters = total_milliliters // 1000
    milliliters = total_milliliters % 1000
    total_volume = liters + milliliters / 1000

    result = total_volume
    return result

print(solution())