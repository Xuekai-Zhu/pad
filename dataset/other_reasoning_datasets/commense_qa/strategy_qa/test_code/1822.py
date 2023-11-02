def solution():
    david_height = 5.0
    average_male_height = 5.75
    tallest_male_height = 8.92
    sistine_chapel_ceiling_height = 68.0
    
    # Calculate the total height from David's head to the ceiling
    total_height = david_height + tallest_male_height + (sistine_chapel_ceiling_height - david_height - average_male_height)
    
    if total_height <= tallest_male_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())