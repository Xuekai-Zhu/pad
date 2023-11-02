def solution():
    total_vehicles = 50 + 40  # Carmen sees 50 trucks and 40 cars
    red_trucks = 0.5 * 50  # Half the trucks are red
    black_trucks = 0.2 * 50  # 20% of the trucks are black
    white_trucks = 50 - red_trucks - black_trucks  # The rest are white trucks
    white_cars = 40 - (total_vehicles - white_trucks)  # The remaining cars are white

    # Calculate the percentage chance that a random vehicle is a white truck
    percentage = (white_trucks / total_vehicles) * 100
    result = round(percentage)
    return result

print(solution())