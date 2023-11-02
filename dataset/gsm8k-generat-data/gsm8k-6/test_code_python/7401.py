def solution():
    # Calculate the amount of water in each tank
    tank1 = 7000 * 3/4
    tank2 = 5000 * 4/5
    tank3 = 3000 * 1/2

    # Calculate the total amount of water in all the tanks
    total_gallons = tank1 + tank2 + tank3
    result = total_gallons
    return result

print(solution())