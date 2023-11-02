def solution():
    # Number of men on board
    men_on_board = 25

    # Water requirements per day
    water_requirement = 0.5 * men_on_board

    # Total water requirements for the entire journey
    total_water_req = water_requirement * 4000

    # Total gallons of water needed
    gallons_of_water = total_water_req / 128  # 1 gallon = 128 ounces

    result = gallons_of_water
    return result

print(solution())