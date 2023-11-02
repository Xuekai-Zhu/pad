def solution():
    """Steve bought $25 worth of groceries. He bought a gallon of milk for $3, two boxes of cereal for $3.5 each, 4 bananas for $.25 each, four apples that cost $.5 each and a number of boxes of cookies. The cookies cost twice as much per box as the gallon of milk. How many boxes of cookies did he get?"""
    total_spent = 25
    milk_price = 3
    cereal_price = 3.5
    banana_price = 0.25
    apple_price = 0.5
    cookie_price = milk_price * 2
    total_price = milk_price + (2 * cereal_price) + (4 * banana_price) + (4 * apple_price) + x * cookie_price
    x = (total_spent - total_price) / cookie_price
    result = x
    return result

print(solution())