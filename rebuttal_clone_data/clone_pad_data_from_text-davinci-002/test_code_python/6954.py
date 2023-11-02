def solution():
    
    cups_per_day = 0.5
    cups_per_package = 1
    price_per_package = 2
    packages_needed = cups_per_day / cups_per_package
    total_price = packages_needed * price_per_package
    result = total_price
    
    return result

print(solution())