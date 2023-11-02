def solution():
    total_fish_weight = 8 + 6*2 + 2*12  # Total weight of all the fish caught
    fish_weight_per_person = 2  # Each person will eat 2 pounds of fish
    num_campers = total_fish_weight // fish_weight_per_person  # Integer division to get the number of campers they can feed
    result = num_campers
    return result

print(solution())