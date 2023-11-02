def solution():
    # Let the weight of the fish Peter caught be x
    x = 2
    # Then the weight of the fish Ali caught is 2x
    ali = 2*x
    # And the weight of the fish Joey caught is x+1

    # The total weight of fish is x + 2x + (x+1) = 4x + 1
    # And we know that the total weight is 25 kg, so we can solve for x
    x = (25 - 1) / 4

    # Now we can calculate the weight of the fish Ali caught
    ali = 2*x
    result = ali
    return result

print(solution())