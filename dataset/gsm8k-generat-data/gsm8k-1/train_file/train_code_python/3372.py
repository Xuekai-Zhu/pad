def solution():
    """Shonda is throwing an Easter egg hunt for her 2 kids and their 10 friends. She is also supplying enough eggs for herself and the 7 other adults there to find eggs as well. If there are 15 Easter egg baskets for everyone to share and each ends up holding 12 Easter eggs, when they equally distribute all of the Easter eggs to everyone, how many eggs does each person get?"""
    total_people = 2 + 10 + 7
    total_baskets = 15
    eggs_per_basket = 12
    total_eggs = total_baskets * eggs_per_basket
    eggs_per_person = total_eggs // total_people
    result = eggs_per_person
    return result

print(solution())