def solution():
    num_people_300_years = 847
    num_ships = 3

    # Use a loop to calculate the number of people on each ship, starting from the last one
    current_num_people = num_people_300_years
    for i in range(num_ships, 0, -1):
        current_num_people /= 2
        current_num_people += 1

    # The remaining current_num_people is the number of people on the first ship
    result = current_num_people
    return result

print(solution())