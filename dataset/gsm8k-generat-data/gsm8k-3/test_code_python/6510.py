def solution():
    """Rachel is an artist. She posts a speed painting video each week on her Instagram account to promote her work. To save time, she paints and records 4 videos at a time. It takes her about 1 hour to set up her painting supplies and her camera. Then she records herself painting for 1 hour per painting. She takes another 1 hour to clean up. Each video takes 1.5 hours to edit and post. How long does it take Rachel to produce a speed painting video?"""
    
    # Calculate the total time for one painting
    painting_time = 1 + 1 + 1 + 1 + 1.5
    
    # Multiply the time for one painting by 4 to get the total time for 4 paintings
    total_time = painting_time * 4
    
    # Display the total time
    result = total_time
    return result

print(solution())