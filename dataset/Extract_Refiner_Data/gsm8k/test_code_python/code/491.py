def solution():
    
    # Define the number of hours Charisma works every day and her walking rate
    HOURS_PER_DAY = 8
    WALKING_RATE = 5

    # Calculate the total number of hours Charisma works in 5 days
    total_hours = HOURS_PER_DAY * 5

    # Calculate the total time Charisma spends on reminding her
    reminding_time = total_hours * WALKING_RATE

    # Calculate the total time Charisma spends walking in 5 days
    walking_time = reminding_time * 5

    # Display the total time Charisma spends walking
    result = walking_time
    return result

print(solution())