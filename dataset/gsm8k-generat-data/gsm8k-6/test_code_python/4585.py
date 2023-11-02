def solution():
    # Calculate the number of portions of 200ml milk that Jasmine can pour
    portions = 2 * 1000 // 200  # liters to milliliters and integer division to get whole number of portions
    result = portions
    return result

print(solution())