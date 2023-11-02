def solution():
    adam_candies = 6  # Adam has 6 candies
    james_candies = 3 * adam_candies  # James has 3 times the number of candies Adam has
    rubert_candies = 4 * james_candies  # Rubert has 4 times the number of candies James has

    # Calculate the total number of candies
    total_candies = adam_candies + james_candies + rubert_candies
    result = total_candies
    return result

print(solution())