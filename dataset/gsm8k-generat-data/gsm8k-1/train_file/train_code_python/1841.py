def solution():
    """Carmen is counting the cars that pass by her window. All the cars are either white, black, or red. She sees 50 trucks and 40 cars. Half the trucks are red, and another 20% are black. If she picks one car at random, what is the percentage chance it's a white truck, rounded to the nearest integer?"""
    total_trucks = 50
    red_trucks_percent = 50
    black_trucks_percent = 20
    white_trucks_percent = 100 - red_trucks_percent - black_trucks_percent
    white_trucks = total_trucks * white_trucks_percent / 100
    total_cars = 40
    total_vehicles = total_trucks + total_cars
    probability = white_trucks / total_vehicles * 100
    result = round(probability)
    
    return result

print(solution())