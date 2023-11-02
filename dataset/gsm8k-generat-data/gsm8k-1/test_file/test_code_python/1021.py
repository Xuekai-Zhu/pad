def solution():
    """The Easter egg hunt team hid 100 eggs. The Smith twins each found 30 eggs. All the other eggs except 10 were found by their friends. How many eggs did the friends find?"""
    total_eggs = 100
    smith_twins_eggs = 30 * 2
    eggs_left = total_eggs - smith_twins_eggs - 10
    friends_eggs = eggs_left
    result = friends_eggs
    return result

print(solution())