def solution():
    """Claire is scheduling her day. She has four hours to clean and two hours to cook, then divides the rest of her working day equally between crafting and tailoring. She then sleeps eight hours. If all of this takes place within one day, how many hours did Claire spend crafting?"""
    # Define the hours allotted for cleaning and cooking
    clean_hours = 4
    cook_hours = 2

    # Calculate the total hours available for crafting and tailoring
    total_working_hours = 24 - clean_hours - cook_hours - 8
    crafting_hours = total_working_hours / 2

    # Display the number of hours spent crafting
    result = crafting_hours
    return result

print(solution())