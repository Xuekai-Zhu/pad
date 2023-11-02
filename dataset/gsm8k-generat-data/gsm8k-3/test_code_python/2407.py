def solution():
    """Jane brings 75% as many pieces of bread as treats to feed the live pets at the zoo.
    Wanda brings half as many treats as Jane and three times as many pieces of bread as treats.
    If Wanda brings 90 pieces of bread, what is the total number of pieces of bread and treats that Wanda and Jane brought to the zoo?"""
    
    # Define the percentage of bread Jane brings
    JANE_BREAD_PERCENTAGE = 0.75
    
    # Define the ratio of treats to bread that Wanda brings
    WANDA_TREATS_TO_BREAD_RATIO = 0.5
    
    # Define the bread Wanda brings
    wanda_bread = 90
    
    # Find the number of treats Wanda brings
    wanda_treats = wanda_bread / (3 * WANDA_TREATS_TO_BREAD_RATIO)
    
    # Find the number of bread Jane brings
    jane_bread = wanda_bread / 3
    
    # Find the number of treats Jane brings
    jane_treats = wanda_treats / 0.75
    
    # Find the total number of pieces of bread and treats brought by both Jane and Wanda
    total_bread = jane_bread + wanda_bread
    total_treats = jane_treats + wanda_treats
    
    # Display the total number of pieces of bread and treats
    result = total_bread + total_treats
    return result

print(solution())