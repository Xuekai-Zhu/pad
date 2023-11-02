def solution():
    """Three friends ate a total of 8 pounds of fruit. Mario had 8 ounces of oranges, while Lydia ate 24 ounces of apples. Nicolai ate peaches. How many pounds of peaches did Nicolai eat?"""
    
    # Convert Mario's 8 ounces of oranges to pounds
    mario_oranges = 8 / 16
    
    # Convert Lydia's 24 ounces of apples to pounds
    lydia_apples = 24 / 16
    
    # Calculate the total weight of oranges and apples eaten
    total_weight_oranges_apples = mario_oranges + lydia_apples
    
    # Calculate the weight of peaches eaten by Nicolai
    nicolai_peaches = 8 - total_weight_oranges_apples
    
    # Display the weight of peaches eaten by Nicolai
    result = nicolai_peaches
    return result

print(solution())