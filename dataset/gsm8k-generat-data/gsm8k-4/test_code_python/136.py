def solution():
    """Loraine makes wax sculptures of animals. Large animals take four sticks of wax and small animals take two sticks. She made three times as many small animals as large animals, and she used 12 sticks of wax for small animals. How many sticks of wax did Loraine use to make all the animals?"""
    # Define the number of sticks of wax for a large and small animal
    LARGE_ANIMAL_WAX = 4
    SMALL_ANIMAL_WAX = 2

    # Calculate the number of small animals
    small_animals = 3 * (1/4) # 3 times as many small animals as large animals
    small_animals_wax = small_animals * SMALL_ANIMAL_WAX

    # Calculate the number of large animals
    large_animals = 1/4
    large_animals_wax = large_animals * LARGE_ANIMAL_WAX

    # Calculate the total number of sticks of wax used
    total_wax = small_animals_wax + large_animals_wax

    result = total_wax
    return result

print(solution())