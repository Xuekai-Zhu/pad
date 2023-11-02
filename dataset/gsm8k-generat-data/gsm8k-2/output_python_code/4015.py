def solution():
    """Mary is trying to count the animals in the petting zoo, but they kept moving around so she double-counts 7 sheep and forgets to count 3 pigs. If Mary thinks there are 60 animals, how many are there really?"""
    double_counted_sheep = 7
    uncounted_pigs = 3
    actual_sheep = (60 - double_counted_sheep - uncounted_pigs) / 2
    total_animals = actual_sheep + double_counted_sheep + uncounted_pigs
    result = total_animals
    return result

print(solution())