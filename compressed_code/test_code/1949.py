def solution():
    
    eggs_per_four_person_cake = 2
    eggs_per_eight_person_cake = eggs_per_four_person_cake * 2
    eggs_in_fridge = 3
    eggs_needed = eggs_per_eight_person_cake - eggs_in_fridge
    result = eggs_needed
    return result

print(solution())