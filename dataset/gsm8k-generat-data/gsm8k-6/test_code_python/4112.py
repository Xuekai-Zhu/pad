def solution():
    average_weight = 20  # pounds of bacon from an average pig
    price_per_pound = 6  # dollars per pound
    runt_weight = average_weight / 2  # pounds of bacon from the runt pig
    total_earnings = runt_weight * price_per_pound  # total dollars earned from the runt pig's bacon
    result = total_earnings
    return result

print(solution())