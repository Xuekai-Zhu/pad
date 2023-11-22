def solution():
    
    # Define the total number of sheep
    total_sheep = 30

    # Calculate the number of sheep Mary gets from half
    half_sheep = total_sheep / 2

    # Calculate the amount of milk Mary gets from the other half every day
    other_half_sheep = half_sheep * 2

    # Calculate the total amount of milk Mary collects every day
    total_sheep_collected = half_sheep + other_half_sheep

    # Display the total amount of milk Mary collects every day
    result = total_sheep_collected
    return result

print(solution())