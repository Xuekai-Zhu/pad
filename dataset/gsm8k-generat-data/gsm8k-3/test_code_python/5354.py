def solution():
    """It was time for Kelly to harvest her carrots that she had planted in three different beds. 
    In the first bed she pulled out 55 carrots. In the second bed she pulled out 101 carrots 
    and in the third bed she pulled out 78 carrots. She found that 6 carrots weighed one pound. 
    How many pounds of carrots did Kelly harvest?"""
    
    # Define the number of carrots in each bed
    bed1_carrots = 55
    bed2_carrots = 101
    bed3_carrots = 78
    
    # Calculate the total number of carrots
    total_carrots = bed1_carrots + bed2_carrots + bed3_carrots
    
    # Calculate the total weight of the carrots in pounds
    weight_in_pounds = total_carrots / 6
    
    # Display the weight in pounds
    result = weight_in_pounds
    return result

print(solution())