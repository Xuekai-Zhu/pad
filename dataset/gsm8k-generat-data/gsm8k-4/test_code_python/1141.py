def solution():
    """A pet store owner had 12 birds, 9 puppies, 5 cats, and 15 spiders. Half the birds were sold and 3 puppies were adopted. Then, someone left the spider enclosure open and 7 of them went loose. How many animals does the pet store owner have left?"""
    # Define the initial number of animals
    birds = 12
    puppies = 9
    cats = 5
    spiders = 15

    # Sell half the birds
    birds_sold = birds // 2
    birds -= birds_sold

    # Adopt 3 puppies
    puppies -= 3

    # Let 7 spiders loose
    spiders -= 7

    # Calculate the total number of animals remaining
    total_remaining = birds + puppies + cats + spiders

    # return the result
    result = total_remaining
    return result

print(solution())