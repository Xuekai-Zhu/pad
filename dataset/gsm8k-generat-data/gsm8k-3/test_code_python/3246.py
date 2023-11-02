def solution():
    """An iron bar measures 12 cm by 8 cm by  6 cm. A factory wants to melt ten iron bars and mold them into iron balls. Each iron ball has a volume of 8 cubic cm. How many iron balls have been molded?"""
    
    # Define the dimensions of the iron bar
    length = 12
    width = 8
    height = 6
    
    # Calculate the volume of the iron bar
    volume_per_bar = length * width * height
    
    # Calculate the total volume of the ten iron bars
    total_volume = volume_per_bar * 10
    
    # Calculate the number of iron balls that can be molded with the total volume
    number_of_balls = total_volume // 8
    
    # Display the number of iron balls molded
    result = number_of_balls
    return result

print(solution())