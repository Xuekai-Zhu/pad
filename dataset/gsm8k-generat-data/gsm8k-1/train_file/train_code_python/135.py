def solution():
    """Loraine makes wax sculptures of animals. Large animals take four sticks of wax and small animals take two sticks. She made three times as many small animals as large animals, and she used 12 sticks of wax for small animals. How many sticks of wax did Loraine use to make all the animals?"""
    small_animal_sticks = 2
    large_animal_sticks = 4
    small_animal_multiplier = 3
    small_animal_total = 12
    large_animal_total = small_animal_total / small_animal_multiplier
    total_sticks = (small_animal_total * small_animal_sticks) + (large_animal_total * large_animal_sticks)
    result = total_sticks
    return result

print(solution())