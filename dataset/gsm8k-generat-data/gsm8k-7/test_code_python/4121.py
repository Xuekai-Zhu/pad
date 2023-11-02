def solution():
    fresh_milk_percentage = 0.8  # 20% spoiled milk
    fresh_egg_percentage = 0.4  # 60% rotten eggs
    fresh_flour_percentage = 0.75  # 1/4 have weevils

    # Probability of getting fresh milk, egg, and flour
    prob_fresh_milk = fresh_milk_percentage
    prob_fresh_egg = fresh_egg_percentage
    prob_fresh_flour = fresh_flour_percentage

    prob_all_fresh = prob_fresh_milk * prob_fresh_egg * prob_fresh_flour
    result = prob_all_fresh
    return result

print(solution())