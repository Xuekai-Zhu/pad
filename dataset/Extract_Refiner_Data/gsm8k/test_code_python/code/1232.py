def solution():
    
    # Define the number of grapes Madeline ate
    madeline_grapes = 6

    # Calculate the number of grapes used for the grape juice
    grape_juice_grapes = 5 * madeline_grapes

    # Calculate the number of grapes remaining after Madeline's grapes are used
    remaining_grapes = madeline_grapes + grape_juice_grapes

    # Calculate the number of grapes used for the pies
    pie_grapes = 12 * 4

    # Calculate the number of grapes at the beginning
    beginning_grapes = remaining_grapes + pie_grapes

    # Display the number of grapes at the beginning
    result = beginning_grapes
    return result

print(solution())