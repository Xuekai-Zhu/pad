def solution():
    dog_fish = 40  # Keanu gave his dog 40 fish
    cat_fish = dog_fish / 2  # Keanu gave his cat half as many fish as he gave to his dog
    total_fish = dog_fish + cat_fish  # Calculate the total number of fish purchased
    cost_per_fish = 4  # Each fish cost Keanu $4
    total_cost = total_fish * cost_per_fish  # Calculate the total cost of the fish

    result = total_cost
    return result

print(solution())