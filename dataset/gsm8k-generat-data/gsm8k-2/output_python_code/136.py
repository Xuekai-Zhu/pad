def solution():
    """Loraine makes wax sculptures of animals. Large animals take four sticks of wax and small animals take two sticks. She made three times as many small animals as large animals, and she used 12 sticks of wax for small animals. How many sticks of wax did Loraine use to make all the animals?"""
    small_animal_wax = 2
    large_animal_wax = 4
    small_animal_count = 3  # three times as many small animals as large animals
    large_animal_count = 1
    total_small_wax = 12
    total_large_wax = large_animal_count * large_animal_wax
    total_animals = small_animal_count + large_animal_count
    total_wax = total_small_wax + total_large_wax
    while total_small_wax > small_animal_count * small_animal_wax:
        large_animal_count += 1
        total_large_wax = large_animal_count * large_animal_wax
        total_animals = small_animal_count + large_animal_count
        total_wax = total_small_wax + total_large_wax

    result = total_wax
    return result

print(solution())