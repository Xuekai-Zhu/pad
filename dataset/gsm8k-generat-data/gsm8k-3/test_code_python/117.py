def solution():
    """An aquarium holds an equal number of clownfish and blowfish. 26 of the blowfish stay in their own tank, and the remaining blowfish swim into a display tank. An equal number of clownfish join the blowfish in the display tank, but then a third of these clownfish swim back into their own tank. If the aquarium holds a combined total of 100 fish, how many clownfish are now in the display tank?"""
    # Define the number of blowfish that remained in their own tank
    blowfish_own_tank = 26

    # Calculate the total number of fish in the aquarium
    total_fish = 100

    # Calculate the number of blowfish that swam into the display tank
    blowfish_display_tank = (total_fish - blowfish_own_tank) / 2

    # Calculate the number of clownfish in the aquarium
    clownfish_total = total_fish / 2

    # Calculate the number of clownfish that joined the blowfish in the display tank
    clownfish_display_tank = blowfish_display_tank

    # Calculate the number of clownfish that swam back into their own tank
    clownfish_own_tank = clownfish_display_tank / 3

    # Calculate the number of clownfish now in the display tank
    clownfish_display_tank -= clownfish_own_tank

    # Return the result
    result = clownfish_display_tank
    return result

print(solution())