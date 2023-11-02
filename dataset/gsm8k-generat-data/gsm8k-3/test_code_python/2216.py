def solution():
    """Jenna is adding black dots to a bunch of white blouses. Each blouse gets 20 dots, and each dot takes 10 ml of black dye. How many 400-ml bottles of dye does Jenna need to buy to dye 100 blouses?"""
    # Define the number of dots per blouse and the dye needed per dot
    dots_per_blouse = 20
    dye_per_dot = 10

    # Calculate the total amount of dye needed for all the blouses
    total_dye_needed = dots_per_blouse * dye_per_dot * 100

    # Calculate the number of 400-ml bottles of dye needed
    bottles_needed = total_dye_needed // 400 + (total_dye_needed % 400 > 0)

    # Display the number of bottles needed
    result = bottles_needed
    return result

print(solution())