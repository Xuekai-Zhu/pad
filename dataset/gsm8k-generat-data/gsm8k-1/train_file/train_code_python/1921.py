def solution():
    """Stormi is saving up to buy a bicycle. She washes 3 cars for $10 each. She mows 2 lawns for $13 each. If the bicycle she wants costs $80, how much more money does Stormi need to make to afford the bicycle?"""
    car_washes = 3
    car_price = 10
    lawn_mows = 2
    lawn_price = 13
    bike_price = 80
    total_earned = (car_washes * car_price) + (lawn_mows * lawn_price)
    money_needed = bike_price - total_earned
    result = money_needed
    return result

print(solution())