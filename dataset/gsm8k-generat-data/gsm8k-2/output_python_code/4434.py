def solution():
    """Steve bought $25 worth of groceries. He bought a gallon of milk for $3, two boxes of cereal for $3.5 each, 4 bananas for $.25 each, four apples that cost $.5 each and a number of boxes of cookies. The cookies cost twice as much per box as the gallon of milk. How many boxes of cookies did he get?"""
    milk_price = 3
    cereal_price = 3.5
    banana_price = 0.25
    apple_price = 0.5
    cookies_price = 2 * milk_price
    num_cookies = int((25 - milk_price - 2 * cereal_price - 4 * banana_price - 4 * apple_price) / cookies_price)
    result = num_cookies
    return result

print(solution())