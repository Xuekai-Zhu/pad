def solution():
    
    jewelry_initial_price = 30
    painting_initial_price = 100
    jewelry_new_price = jewelry_initial_price + 10
    painting_new_price = painting_initial_price * 1.2
    total_price = (2 * jewelry_new_price) + (5 * painting_new_price)
    result = total_price
    return result

print(solution())