def solution():
    """Pauline has 125 matchbox cars. They are all either convertibles, trucks, regular cars. 64% of them are regular cars. 8% are trucks. How many convertibles does she own?"""
    total_cars = 125
    regular_cars_percent = 64
    trucks_percent = 8
    convertibles_percent = 100 - regular_cars_percent - trucks_percent
    convertibles_count = total_cars * (convertibles_percent / 100)
    result = convertibles_count
    return result

print(solution())