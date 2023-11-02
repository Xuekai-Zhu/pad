def solution():
    total_fish = 100
    num_blowfish_in_tank = 26
    num_blowfish_in_display = total_fish / 2 - num_blowfish_in_tank

    # Calculate the total number of clownfish in the aquarium
    total_clownfish = total_fish / 2

    # Calculate the number of clownfish in the display tank
    num_clownfish_in_display = total_clownfish / 2

    # Calculate the number of clownfish that swim back to their own tank
    num_clownfish_return_to_tank = num_clownfish_in_display / 3

    # Calculate the final number of clownfish in the display tank
    num_clownfish_in_display -= num_clownfish_return_to_tank
    result = num_clownfish_in_display
    return result

print(solution())