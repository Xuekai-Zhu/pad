def solution():
    """The green piece of yarn is 156 cm long. The red yarn is 8 cm more than three times the length of the green yarn. What is the number of centimeters in the total length for the 2 pieces of yarn?"""
    
    # Define the length of the green yarn
    green_yarn = 156
    
    # Calculate the length of the red yarn
    red_yarn = 3 * green_yarn + 8
    
    # Calculate the total length of yarn
    total_length = green_yarn + red_yarn
    
    # Display the total length of yarn
    result = total_length
    return result

print(solution())