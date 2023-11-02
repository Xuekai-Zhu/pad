def solution():
    starting_number = 300
    seeds_in_water = starting_number / 3
    seeds_eaten_by_insects = starting_number / 6
    seeds_eaten = seeds_in_water + seeds_eaten_by_insects
    seeds_sprouted = (starting_number - seeds_eaten) / 2
    seeds_survived = seeds_sprouted - seeds_eaten
    result = seeds_survived
    return result

print(solution())