def solution():
    """Carmen is counting the cars that pass by her window. All the cars are either white, black, or red. She sees 50 trucks and 40 cars. Half the trucks are red, and another 20% are black. If she picks one car at random, what is the percentage chance it's a white truck, rounded to the nearest integer?"""
    total_trucks = 50
    total_cars = 40
    red_trucks = total_trucks / 2
    black_trucks = total_trucks * 0.2
    white_trucks = total_trucks - red_trucks - black_trucks
    total_white_trucks = white_trucks
    total_cars_white_trucks = total_white_trucks + (total_cars / 3)
    probability = (total_white_trucks / total_cars_white_trucks) * 100
    result = round(probability)
    return result

print(solution())