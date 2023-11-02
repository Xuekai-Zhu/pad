def solution():
    """The elevator in Jack's building supports a maximum load of 700 kg. An adult weighs an average of 80 kg. If Jack rides the elevator with 8 other adults, by how much will they have exceeded the maximum load of the elevator?"""
    max_load = 700
    adult_weight = 80
    num_adults = 8
    total_weight = adult_weight * num_adults
    excess_weight = total_weight - max_load
    result = excess_weight
    return result

print(solution())