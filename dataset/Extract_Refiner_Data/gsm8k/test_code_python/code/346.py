def solution():
    
    # Define the length of each activity in hours
    monday_yoga = 1
    tuesday_yoga = monday_yoga * 3
    wednesday_event = 0.5
    thursday_event = tuesday_yoga / 2
    friday_event = 2

    # Calculate the total length of all activities in hours
    total_time = monday_yoga + tuesday_yoga + wednesday_event + thursday_event + friday_event

    # Display the total time
    result = total_time
    return result

print(solution())