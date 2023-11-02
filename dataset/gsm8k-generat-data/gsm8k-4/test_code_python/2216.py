def solution():
    """Jenna is adding black dots to a bunch of white blouses. Each blouse gets 20 dots, and each dot costs 10 ml of black dye. How many 400-ml bottles of dye does Jenna need to buy to dye 100 blouses?"""
    # Define the number of blouses and dots per blouse
    blouses = 100
    dots_per_blouse = 20

    # Define the amount of dye per dot
    dye_per_dot = 10

    # Calculate the total amount of dye needed
    total_dye = blouses * dots_per_blouse * dye_per_dot

    # Calculate the number of 400-ml bottles of dye needed
    bottles_of_dye = total_dye / 400

    # Round up to the nearest whole number of bottles
    bottles_of_dye = math.ceil(bottles_of_dye)

    result = bottles_of_dye
    return result

print(solution())