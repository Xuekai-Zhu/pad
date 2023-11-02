def solution():
    """Mark has 3 tanks for pregnant fish. Each tank has 4 pregnant fish and each fish gives birth to 20 young. How many young fish does he have at the end?"""
    tanks = 3
    fish_per_tank = 4
    offspring_per_fish = 20
    total_offspring = tanks * fish_per_tank * offspring_per_fish
    result = total_offspring
    return result

print(solution())