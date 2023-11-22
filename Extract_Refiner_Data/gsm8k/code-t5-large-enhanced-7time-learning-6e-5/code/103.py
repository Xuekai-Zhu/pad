def solution():
    
    # Define the length of each episode in minutes
    EPISODE_LENGTH = 1

    # Define the length of show watched on each day
    monday_tuesday_show = EPISODE_LENGTH * 2
    wednesday_show = 30
    thursday_show = 1
    friday_show = 1 * 2

    # Calculate the total length of show watched
    total_show_length = monday_tuesday_show + wednesday_show + thursday_show + friday_show

    # Display the total length watched in minutes
    result = total_show_length
    return result

print(solution())