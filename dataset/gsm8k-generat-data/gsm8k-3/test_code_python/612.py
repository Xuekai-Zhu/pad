def solution():
    """Ali is collecting bottle caps. He has 125 bottle caps. He has red ones and green ones. If he has 50 red caps, what percentage of caps are green?"""
   
   # Define the number of red bottle caps Ali has
    red_caps = 50
    
   # Define the total number of bottle caps Ali has
    total_caps = 125
    
   # Calculate the number of green bottle caps Ali has
    green_caps = total_caps - red_caps
    
   # Calculate the percentage of green bottle caps
    percentage_green_caps = (green_caps/total_caps) * 100
    
   # Display the percentage of green bottle caps
    result = percentage_green_caps
    return result

print(solution())