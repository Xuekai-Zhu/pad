def solution():
    total_trucks = 50
    total_cars = 40

    # Calculate the number of red trucks
    red_trucks = total_trucks / 2

    # Calculate the number of black trucks
    black_trucks = total_trucks * 0.2

    # Calculate the number of white trucks
    white_trucks = total_trucks - red_trucks - black_trucks

    # Calculate the total number of white vehicles
    total_white = white_trucks + (total_cars / 3)

    # Calculate the percentage chance of picking a white truck
    chance_white_truck = (white_trucks / total_white) * 100
    result = round(chance_white_truck)
    return result

print(solution())