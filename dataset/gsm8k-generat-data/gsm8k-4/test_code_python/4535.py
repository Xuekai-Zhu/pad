def solution():
    """There are 26 chickens, 40 piglets, and 34 goats at Stacy’s farm. A really bad storm hits and half of all the animals get sick. How many animals in total get sick?"""
    # Define the starting number of animals
    chickens = 26
    piglets = 40
    goats = 34

    # Calculate the number of sick animals
    sick_animals = (chickens + piglets + goats) / 2

    # Return the result
    result = sick_animals
    return result

print(solution())