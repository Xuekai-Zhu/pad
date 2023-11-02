def solution():
    bottles_per_day = 0.5
    bottles_per_6 pack = 6
    number_of_6 packs = 3
    total_number_of_bottles = number_of_6 packs * bottles_per_6 pack
    bottles_left = total_number_of_bottles - (bottles_per_day * 28)
    result = bottles_left
    return result

print(solution())