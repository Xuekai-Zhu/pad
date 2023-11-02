def solution():
    # Calculate the average lifespan of dogs and the maximum lifespan of fish
    dog_lifespan = 4 * 2.5  # dogs live on average 4 times as long as hamsters, which live an average of 2.5 years
    fish_lifespan = dog_lifespan + 2  # well-cared fish can live 2 years longer than dogs live
    result = fish_lifespan
    return result

print(solution())