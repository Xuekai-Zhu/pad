def solution():
    # Determine how many candies each person has
    adam_candies = 6
    james_candies = 3 * adam_candies
    rubert_candies = 4 * james_candies

    # Find the total number of candies the three have together
    total_candies = adam_candies + james_candies + rubert_candies
    result = total_candies
    return result

print(solution())