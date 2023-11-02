def solution():
    """McKenna has 34 stuffed animals. Kenley has twice as many as McKenna.  Tenly has 5 more than Kenley . How many stuffed animals do the three girls have in all?"""
    # Define the number of stuffed animals each girl has
    mckenna_animals = 34
    kenley_animals = mckenna_animals * 2
    tenly_animals = kenley_animals + 5

    # Calculate the total number of stuffed animals
    total_animals = mckenna_animals + kenley_animals + tenly_animals

    # Display the total number of stuffed animals
    result = total_animals
    return result

print(solution())