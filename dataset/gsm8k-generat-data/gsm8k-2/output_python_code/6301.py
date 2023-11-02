def solution():
    """Pauline has 125 matchbox cars. They are all either convertibles, trucks, regular cars. 64% of them are regular cars. 8% are trucks. How many convertibles does she own?"""
    total_cars = 125
    regular_cars_percent = 0.64
    truck_percent = 0.08
    regular_cars = total_cars * regular_cars_percent
    trucks = total_cars * truck_percent
    convertibles = total_cars - regular_cars - trucks
    result = convertibles
    return result

print(solution())