def solution():
    """By the time Anne is two times as old as Emile, Emile will be six times as old as Maude. If Maude will be 8 years old, how old will Anne be?"""
    maude_age = 8
    emile_age = maude_age * 6 / 1
    anne_age = emile_age * 2
    result = anne_age
    return result

print(solution())