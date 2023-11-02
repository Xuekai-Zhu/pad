def solution():
    parakeets = 3
    parrots = 2
    finches = 4
    parakeet_food = 2 * parakeets * 7
    parrot_food = 14 * parrots * 7
    finch_food = 0.5 * 2 * finches * 7  # Each finch eats half of what a parakeet eats
    total_food = parakeet_food + parrot_food + finch_food
    result = total_food
    return result

print(solution())