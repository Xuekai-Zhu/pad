def solution():
    """Stormi is saving up to buy a bicycle. She washes 3 cars for $10 each. She mows 2 lawns for $13 each. If the bicycle she wants costs $80, how much more money does Stormi need to make to afford the bicycle?"""
    car_wash_money = 3 * 10
    lawn_mowing_money = 2 * 13
    total_money = car_wash_money + lawn_mowing_money
    needed_money = 80 - total_money
    result = needed_money
    return result

print(solution())