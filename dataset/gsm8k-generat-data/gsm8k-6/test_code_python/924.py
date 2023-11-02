def solution():
    # Calculate the time required to wash all 8 loads of laundry
    wash_time = 8 * 0.75  # each load takes 45 minutes to wash (0.75 hours)
    
    # Calculate the time required to dry all 8 loads of laundry
    dry_time = 8 * 1  # each load takes 1 hour to dry
    
    # Calculate the total time required
    total_time = wash_time + dry_time
    
    # Convert the time to hours
    total_time_hours = total_time / 60
    
    result = total_time_hours
    return result

print(solution())