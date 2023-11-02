def solution():
    """The recipe for a four-person cake requires 2 eggs and 4 cups of milk. Tyler wants to use this recipe to make a cake for eight people. If Tyler has 3 eggs in the fridge, how many more eggs does Tyler need to buy?"""
    eggs_per_four_person_cake = 2
    eggs_per_eight_person_cake = eggs_per_four_person_cake * 2
    eggs_in_fridge = 3
    eggs_needed = eggs_per_eight_person_cake - eggs_in_fridge
    result = eggs_needed
    return result

print(solution())