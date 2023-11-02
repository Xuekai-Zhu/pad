def solution():
    num_fish = 6  # Jason starts with 6 fish in his aquarium
    num_fish *= 2  # On the second day, the number of fish doubles
    num_fish *= 2  # On the third day, the number of fish doubles again
    num_fish *= 2  # On the fourth day, the number of fish doubles again
    num_fish *= (2/3)  # On the third day, Jason takes out one-third of the fish
    num_fish *= 2  # On the fifth day, the number of fish doubles again
    num_fish *= (3/4)  # On the fifth day, Jason takes out one-fourth of the fish
    num_fish += 15  # On the seventh day, Jason adds 15 more fish

    result = num_fish
    return result

print(solution())