def solution():
    # Calculate the total time spent on the road by William
    total_time = (8 - 7) * 60  # William left at 7:00 AM and arrived at 8:00 PM, so he spent (8-7)*60=60 minutes on the road
    
    # Subtract the time spent on the stops
    total_time -= (25 + 10 + 25)  # William had 3 stops of 25, 10 and 25 minutes respectively
    
    # Convert the total time to hours
    total_hours = total_time / 60

    result = total_hours
    return result

print(solution())