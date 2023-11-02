def solution():
    """Martha's cat catches 3 rats and 7 birds. Cara's cat catches 3 less than five times as many animals as Martha's cat. How many animals does Cara's cat catch?"""
    # Define the number of animals caught by Martha's cat
    martha_animals = 3 + 7

    # Calculate the number of animals caught by Cara's cat
    cara_animals = (5 * martha_animals) - 3

    # return the result
    result = cara_animals
    return result

print(solution())