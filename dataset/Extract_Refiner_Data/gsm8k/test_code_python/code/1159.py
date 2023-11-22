def solution():
    
    # Define the number of times Tyrion goes out each day
    times_per_day = 3

    # Define the number of face masks Tyrion changes his mask every time he goes out
    masks_per_change = 2

    # Calculate the total number of face masks Tyrion uses every 2 days
    total_masks = times_per_day * masks_per_change * 2

    # Display the total number of face masks
    result = total_masks
    return result

print(solution())