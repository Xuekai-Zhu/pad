def solution():
    bikes_wheels = 2 * 20 # Each bike has 2 wheels
    cars_wheels = 4 * 10 # Each car has 4 wheels
    motos_wheels = 2 * 5  # Each motorcycle has 2 wheels

    # Total wheels in the garage
    total_wheels = bikes_wheels + cars_wheels + motos_wheels
    result = total_wheels
    return result

print(solution())