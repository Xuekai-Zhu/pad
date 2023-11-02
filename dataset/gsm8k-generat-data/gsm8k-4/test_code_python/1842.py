def solution():
    """Carmen is counting the cars that pass by her window. All the cars are either white, black, or red. She sees 50 trucks and 40 cars. Half the trucks are red, and another 20% are black. If she picks one car at random, what is the percentage chance it's a white truck, rounded to the nearest integer?"""
    # Define the number of trucks and cars
    total_trucks = 50
    total_cars = 40

    # Calculate the number of red trucks
    red_trucks = total_trucks * 0.5

    # Calculate the number of black trucks
    black_trucks = total_trucks * 0.2

    # Calculate the number of white trucks
    white_trucks = total_trucks - red_trucks - black_trucks

    # Calculate the percentage chance of picking a white truck
    p_white_truck = (white_trucks / total_cars) * 100

    # Round the result to the nearest integer
    result = round(p_white_truck)

    return result

print(solution())