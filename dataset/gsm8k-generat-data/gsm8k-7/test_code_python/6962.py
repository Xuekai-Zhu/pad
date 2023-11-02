def solution():
    num_dog_fish = 40
    cat_fish_ratio = 0.5
    fish_cost = 4

    # Calculate the number of fish Keanu gave to his cat
    num_cat_fish = cat_fish_ratio * num_dog_fish

    # Calculate the total number of fish Keanu bought
    total_fish = num_dog_fish + num_cat_fish

    # Calculate the total cost of all the fish Keanu bought
    total_cost = total_fish * fish_cost
    result = total_cost
    return result

print(solution())