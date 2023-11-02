def solution():
    # Calculate the remaining number of fish
    remaining_guppies = 94 - 30
    remaining_angelfish = 76 - 48
    remaining_tigersharks = 89 - 17
    remaining_oscarfish = 58 - 24
    total_remaining_fish = remaining_guppies + remaining_angelfish + remaining_tigersharks + remaining_oscarfish
    result = total_remaining_fish
    return result

print(solution())