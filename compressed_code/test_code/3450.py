def solution():
    
    milk_price = 3
    cereal_price = 3.5
    banana_price = 0.25
    apple_price = 0.5
    cookies_price = 2 * milk_price
    num_cookies = int((25 - milk_price - 2 * cereal_price - 4 * banana_price - 4 * apple_price) / cookies_price)
    result = num_cookies
    return result

print(solution())