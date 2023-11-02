def solution():
    total_weight = 25
    
    # Let x be the weight of the fish that Peter caught
    # Then the weight of the fish that Ali caught is 2x
    # And the weight of the fish that Joey caught is x + 1

    x = (total_weight - 1) / 4 # Using the fact that the three of them caught a total of 25 kg of fish
    ali_weight = 2 * x
    
    result = ali_weight
    return result

print(solution())