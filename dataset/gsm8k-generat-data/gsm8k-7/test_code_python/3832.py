def solution():
    num_seeds_per_color = 125
    surviving_red_flowers = num_seeds_per_color - 45
    surviving_yellow_flowers = num_seeds_per_color - 61
    surviving_orange_flowers = num_seeds_per_color - 30
    surviving_purple_flowers = num_seeds_per_color - 40

    total_surviving_flowers = sum([surviving_red_flowers, surviving_yellow_flowers, surviving_orange_flowers, surviving_purple_flowers])

    # Calculate the number of bouquets that can be made
    num_bouquets = total_surviving_flowers // 9

    result = num_bouquets
    return result

print(solution())