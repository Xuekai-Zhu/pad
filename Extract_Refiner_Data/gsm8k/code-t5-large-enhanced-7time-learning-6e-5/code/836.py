def solution():
    
    # Define the length of the original glue stick
    ORIGINAL_LENGTH = 12000

    # Calculate the length of the three glue sticks that are partially used
    used_length = ORIGINAL_LENGTH * (1/6) + (2/3) + ORIGINAL_LENGTH * (1/2)

    # Calculate the length of the glue sticks that are not used
    unused_length = ORIGINAL_LENGTH - used_length

    # Display the length of the glue sticks that are not used
    result = unused_length
    return result

print(solution())