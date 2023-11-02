def solution():
    # Calculate the probability of all three ingredients being good
    milk_fresh = 0.8  # probability of a bottle of milk being fresh
    eggs_fresh = 0.4  # probability of an egg being not rotten
    flour_good = 0.75  # probability of a canister of flour not having weevils
    probability = milk_fresh * eggs_fresh * flour_good
    result = probability
    return result

print(solution())