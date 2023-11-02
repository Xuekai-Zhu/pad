def solution():
    """It takes 7 years for an apple tree to bear fruit. If Lydia planted a tree when she was 4 years old and is now 9 years old, how old would she be when she gets to eat an apple from her tree for the first time?"""
    # Define Lydia's current age and the age she was when she planted the tree
    current_age = 9
    planting_age = 4

    # Calculate the number of years until the tree bears fruit
    fruit_age = planting_age + 7

    # Calculate Lydia's age when the tree bears fruit
    age_when_fruit = current_age + (fruit_age - planting_age)

    result = age_when_fruit
    return result

print(solution())