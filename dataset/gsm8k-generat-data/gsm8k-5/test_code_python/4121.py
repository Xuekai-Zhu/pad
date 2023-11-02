def solution():
    # Probability of getting fresh milk
    fresh_milk_prob = 0.8

    # Probability of getting a good egg
    good_egg_prob = 0.4

    # Probability of getting flour without weevils
    flour_prob = 0.75

    # Probability of getting all three good ingredients
    probability = fresh_milk_prob * good_egg_prob * flour_prob

    result = probability
    return result

print(solution())