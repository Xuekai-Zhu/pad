def solution():
    # Calculate the number of blowfish in the aquarium
    total_fish = 100
    blowfish_in_tank = 26
    blowfish_display = total_fish // 2 - blowfish_in_tank

    # Calculate the number of clownfish in the display tank
    clownfish_display = blowfish_display // 2
    clownfish_back = clownfish_display // 3
    clownfish_display_final = clownfish_display - clownfish_back

    result = clownfish_display_final
    return result

print(solution())