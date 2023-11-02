def solution():
    """Rupert has 4 times the number of candies James has. James has 3 times the number of candies Adam has. If Adam has 6 candies, how many candies do the three of them have in total?"""
    # Define the number of candies Adam has
    adam_candies = 6

    # Calculate the number of candies James has
    james_candies = 3 * adam_candies

    # Calculate the number of candies Rupert has
    rupert_candies = 4 * james_candies

    # Calculate the total number of candies
    total_candies = adam_candies + james_candies + rupert_candies

    # Display the total number of candies
    result = total_candies
    return result

print(solution())