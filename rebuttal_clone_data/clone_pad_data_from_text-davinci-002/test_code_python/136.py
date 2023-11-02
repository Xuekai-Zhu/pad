def solution():
    """Loraine makes wax sculptures of animals. Large animals take four sticks of wax and small animals take two sticks. She made three times as many small animals as large animals, and she used 12 sticks of wax for small animals. How many sticks of wax did Loraine use to make all the animals?"""
    large_animal_wax = 4
    small_animal_wax = 2
    large_animal_number = (12 / small_animal_wax) / 3
    total_wax = (large_animal_wax * large_animal_number) + (small_animal_wax * 12)
    result = total_wax
    return result

print(solution())