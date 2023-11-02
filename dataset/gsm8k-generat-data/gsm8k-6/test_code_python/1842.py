def solution():
    # Calculate the number of black and red trucks
    total_trucks = 50
    red_trucks = total_trucks / 2
    black_trucks = total_trucks * 0.2

    # Calculate the number of white trucks
    white_trucks = total_trucks - red_trucks - black_trucks

    # Calculate the percentage chance of picking a white truck
    total_cars = 40 + total_trucks
    chance_of_white_truck = (white_trucks / total_cars) * 100
    result = round(chance_of_white_truck)
    return result

print(solution())