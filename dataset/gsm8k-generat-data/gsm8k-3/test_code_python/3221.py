def solution():
    """Kay has 14 siblings.  Kay is 32 years old.  The youngest sibling is 5 less than half Kay's age.  The oldest sibling is four times as old as the youngest sibling.  How old is the oldest sibling?"""
    # Calculate the youngest sibling's age
    youngest = 0.5 * 32 - 5

    # Calculate the oldest sibling's age
    oldest = 4 * youngest
    
    # Add 14 to account for all siblings, including Kay
    siblings = 14
    
    # Calculate the average age of all the siblings
    sibling_average = (sum(range(1, siblings+1)) + 32 + youngest + oldest) / (siblings + 2)
    
    # Calculate the age of the oldest sibling by subtracting the total age of all siblings (including Kay) from the sum of Kay's age and the youngest sibling's age multiplied by 2, then subtracting that result from the total age of all the siblings
    oldest = sibling_average * (siblings + 2) - 32 - (youngest * 2)
    
    # Display the age of the oldest sibling
    result = oldest
    return result

print(solution())