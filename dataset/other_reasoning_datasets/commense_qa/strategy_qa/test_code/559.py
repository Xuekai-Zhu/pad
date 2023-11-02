def solution():
    car_methane_production = 2.7
    cow_methane_production = 4.0
    if cow_methane_production < car_methane_production:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())