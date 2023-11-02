def solution():
    """Keanu bought some fish from the store for his pets. He gave his cat half as many fish as he gave to his dog. If he gave his dog 40 fish, and each fish cost him $4, calculate the total amount of money he spent at the store to buy all the fish."""
    dog_fish = 40
    cat_fish = dog_fish / 2
    total_fish = dog_fish + cat_fish
    fish_cost = 4
    total_cost = total_fish * fish_cost
    result = total_cost
    return result

print(solution())