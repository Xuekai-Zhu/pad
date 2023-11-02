def solution():
    """Sophia ate 1/6 of her pie and she put the rest on the fridge. If the pie left in the fridge weighs 1200 grams, how many grams did Sophia eat?"""
    # Calculate the weight of the whole pie
    weight_whole_pie = 1200 * 6 / 5
    
    # Calculate the weight Sophia ate
    weight_eaten = weight_whole_pie / 6
    
    # Display the weight Sophia ate
    result = weight_eaten
    return result

print(solution())