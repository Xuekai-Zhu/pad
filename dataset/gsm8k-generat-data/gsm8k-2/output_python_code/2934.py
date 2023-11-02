def solution():
    """Edward had $17.80 to spend at the toy store. He bought 4 toy cars that cost $0.95 each and a race track that cost $6.00. How much money does he have left to buy more toys?"""
    initial_money = 17.8
    toy_car_cost = 0.95
    race_track_cost = 6
    toys_cost = 4 * toy_car_cost + race_track_cost
    remaining_money = initial_money - toys_cost
    result = remaining_money
    return result

print(solution())