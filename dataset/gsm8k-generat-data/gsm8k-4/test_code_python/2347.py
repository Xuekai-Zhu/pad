def solution():
    """Rubert has 4 times the number of candies James has. James has 3 times the number of candies Adam has. If Adam has 6 candies, how many candies do the three of them have in total?"""
    # Define the initial number of candies
    adam_candies = 6

    # Calculate the number of candies James has
    james_candies = adam_candies * 3

    # Calculate the number of candies Rubert has
    rubert_candies = james_candies * 4

    # Calculate the total number of candies
    total_candies = adam_candies + james_candies + rubert_candies

    # return the result
    result = total_candies
    return result

print(solution())