def solution():
    """Carmen is counting the cars that pass by her window. All the cars are either white, black, or red. She sees 50 trucks and 40 cars. Half the trucks are red, and another 20% are black. If she picks one car at random, what is the percentage chance it's a white truck, rounded to the nearest integer?"""
    # Define the number of trucks and cars
    trucks = 50
    cars = 40

    # Calculate the number of red trucks and black trucks
    red_trucks = trucks / 2
    black_trucks = trucks * 0.2

    # Calculate the number of white trucks
    white_trucks = trucks - red_trucks - black_trucks

    # Calculate the total number of cars
    total_cars = trucks + cars

    # Calculate the percentage chance of picking a white truck
    chance = (white_trucks / total_cars) * 100

    # Round the percentage chance to the nearest integer
    rounded_chance = round(chance)

    # Display the percentage chance
    result = rounded_chance
    return result

print(solution())