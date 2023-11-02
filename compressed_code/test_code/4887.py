def solution():
    
    salad_price = 3
    beef_price = 2 * salad_price
    potato_price = salad_price / 3
    juice_price = 1.5
    total_price = (2 * salad_price) + (2 * beef_price) + (1 * potato_price) + (2 * juice_price)
    result = total_price
    return result

print(solution())