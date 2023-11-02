def solution():
    # Calculate the number of red and black trucks
    red_trucks = 0.5 * 50
    black_trucks = 0.2 * 50

    # Calculate the number of white trucks
    white_trucks = 50 - red_trucks - black_trucks

    # Calculate the total number of white cars
    total_white_cars = white_trucks + 0.5 * (40 - 50)

    # Calculate the percentage chance of choosing a white truck
    chance_of_white_truck = (white_trucks / total_white_cars) * 100

    result = round(chance_of_white_truck)
    return result

print(solution())