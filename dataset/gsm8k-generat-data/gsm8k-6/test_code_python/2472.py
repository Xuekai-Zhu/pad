def solution():
    # Calculate the probability of packing a ham sandwich and a cake on the same day
    # Probability of packing ham sandwich = 3/5 (since there are 3 school days out of 5)
    # Probability of packing cake on any given day = 1/5
    # Probability of packing both on the same day = (3/5) * (1/5) = 3/25
    # Convert to percentage
    probability = (3/25) * 100
    result = probability
    return result

print(solution())