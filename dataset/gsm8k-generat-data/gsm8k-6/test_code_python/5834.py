def solution():
    # Find the number of cars parked in the back parking lot
    cars_in_back = 38 * 0.5  # 1/2 of the spaces in the back parking lot are filled
    total_parked = cars_in_back + 39  # total number of cars parked
    total_spaces = 52 + 38  # total number of parking spaces
    spaces_available = total_spaces - total_parked  # number of parking spaces still available
    result = spaces_available
    return result

print(solution())