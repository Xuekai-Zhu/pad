def solution():
    """Claire is scheduling her day. She has four hours to clean and two hours to cook, then divides the rest of her working day equally between crafting and tailoring. She then sleeps eight hours. If all of this takes place within one day, how many hours did Claire spend crafting?"""
    total_hours = 24
    cleaning_time = 4
    cooking_time = 2
    sleeping_time = 8
    working_time = total_hours - cleaning_time - cooking_time - sleeping_time
    crafting_time = working_time / 2
    result = crafting_time
    return result

print(solution())