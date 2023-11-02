def solution():
    """Rubert has 4 times the number of candies James has. James has 3 times the number of candies Adam has. If Adam has 6 candies, how many candies do the three of them have in total?"""
    adam_candies = 6
    james_candies = 3 * adam_candies
    rubert_candies = 4 * james_candies
    
    total_candies = adam_candies + james_candies + rubert_candies
    result = total_candies
    return result

print(solution())