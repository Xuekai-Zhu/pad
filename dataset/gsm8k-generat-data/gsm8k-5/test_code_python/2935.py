def solution():
    toy_car_cost = 0.95  # Each toy car costs $0.95
    num_toy_cars = 4  # Edward bought 4 toy cars
    race_track_cost = 6.00  # The race track costs $6.00
    total_cost = (toy_car_cost * num_toy_cars) + race_track_cost  # Calculate the total cost

    # Calculate how much money Edward has left after buying the toys
    money_left = 17.80 - total_cost
    result = money_left
    return result

print(solution())