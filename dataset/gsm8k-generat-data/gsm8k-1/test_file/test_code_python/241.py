def solution():
    """There are 4 snails in one aquarium and 32 snails in another aquarium. The difference between the number of snails in the two aquariums is twice the amount of fish in both aquariums. If both aquariums have the same number of fish in them, how many fish are there in each aquarium?"""
    snails_aquarium_1 = 4
    snails_aquarium_2 = 32
    fish_total = (snails_aquarium_2 - snails_aquarium_1) / 2
    fish_per_aquarium = fish_total / 2
    result = fish_per_aquarium
    return result

print(solution())