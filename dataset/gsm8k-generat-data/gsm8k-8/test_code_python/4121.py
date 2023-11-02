def solution():
    # Define the probabilities of each ingredient being good
    good_flour_prob = 0.75
    good_milk_prob = 0.8
    good_egg_prob = 0.4

    # Calculate the probability of all three ingredients being good
    probability_all_good = good_flour_prob * good_milk_prob * good_egg_prob
    result = probability_all_good
    return result

print(solution())