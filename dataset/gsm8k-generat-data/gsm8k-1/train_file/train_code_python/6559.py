def solution():
    """Three friends ate a total of 8 pounds of fruit. Mario had 8 ounces of oranges, while Lydia ate 24 ounces of apples. Nicolai ate peaches. How many pounds of peaches did Nicolai eat?"""
    total_fruit = 8 #in pounds
    mario_oranges = 8/16 #in pounds
    lydia_apples = 24/16 #in pounds
    nicolai_peaches = total_fruit - mario_oranges - lydia_apples 
    result = nicolai_peaches
    return result

print(solution())