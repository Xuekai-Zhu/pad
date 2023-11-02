def solution():
    """Claire is scheduling her day. She has four hours to clean and two hours to cook, then divides the rest of her working day equally between crafting and tailoring. She then sleeps eight hours. If all of this takes place within one day, how many hours did Claire spend crafting?"""
    # Define the number of hours Claire has in a day
    total_hours = 24

    # Define the number of hours for cleaning and cooking
    cleaning_hours = 4
    cooking_hours = 2

    # Calculate the number of hours Claire has left for crafting and tailoring
    crafting_tailoring_hours = total_hours - cleaning_hours - cooking_hours - 8

    # Calculate the number of hours Claire spends on crafting
    crafting_hours = crafting_tailoring_hours / 2

    result = crafting_hours
    return result

print(solution())