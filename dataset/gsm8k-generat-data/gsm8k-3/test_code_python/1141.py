def solution():
    """A pet store owner had 12 birds, 9 puppies, 5 cats, and 15 spiders. Half the birds were sold and 3 puppies were adopted. Then, someone left the spider enclosure open and 7 of them went loose. How many animals does the pet store owner have left?"""
    # Define the initial number of each type of animal
    birds = 12
    puppies = 9
    cats = 5
    spiders = 15

    # Calculate the new number of animals after some were sold or adopted
    birds = birds // 2
    puppies -= 3

    # Calculate the new number of spiders after some escaped
    spiders -= 7

    # Calculate the total number of animals left
    total_animals = birds + puppies + cats + spiders

    # Display the total number of animals left
    result = total_animals
    return result

print(solution())