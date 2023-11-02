def solution():
    
    # Define the dimensions of the hole
    length = 6
    width = 4
    depth = 3

    # Calculate the volume of the hole
    volume = length * width * depth

    # Calculate the time it will take to shovel the earth
    time = volume * 3

    # Display the time it will take to dig the hole
    result = time
    return result

print(solution())