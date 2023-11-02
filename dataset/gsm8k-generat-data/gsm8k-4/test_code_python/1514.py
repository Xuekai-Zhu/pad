def solution():
    """Carla spends 10 minutes sharpening her knife and 3 times that amount of time peeling vegetables. How much time does she spend on these activities total?"""
    # Define the time in minutes to sharpen the knife
    knife_sharpening_time = 10
    
    # Calculate the time in minutes to peel vegetables
    vegetable_peeling_time = knife_sharpening_time * 3
    
    # Calculate the total time spent on both activities
    total_time = knife_sharpening_time + vegetable_peeling_time
    
    # Return the result
    result = total_time
    return result

print(solution())