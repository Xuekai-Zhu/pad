def solution():
    # Convert 1 hour 20 minutes to minutes
    train_time = 80
    # Convert train time to hours and minutes
    train_hours = train_time // 60
    train_minutes = train_time % 60
    
    # Add train time to time spent walking
    total_time = train_time + 10
    
    # Convert total time to hours and minutes
    total_hours = total_time // 60
    total_minutes = total_time % 60
    
    # Calculate the time Pete needs to leave by
    leave_hours = 9 - total_hours
    leave_minutes = 60 - total_minutes
    
    # Adjust leave time if necessary
    if leave_minutes >= 60:
        leave_hours -= 1
        leave_minutes -= 60
    
    # Format leave time as 24-hour time string
    leave_time = "{:02d}:{:02d}".format(leave_hours, leave_minutes)
    
    result = leave_time
    return result

print(solution())