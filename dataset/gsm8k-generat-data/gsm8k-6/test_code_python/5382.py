def solution():
    # Calculate the total length of TV episodes and movies Emily watches
    total_watching_time = 3*25 + 2*(1*60 + 45)  # 3 TV episodes of 25 minutes each, 2 movies of 1 hour and 45 minutes each

    # Calculate the total time Emily spends on activities
    total_activities_time = total_watching_time + 4.5*60  # 4.5 hours of sleep converted to minutes

    # Calculate the remaining time in the flight
    remaining_time = (10*60) - total_activities_time  # 10 hours of flight converted to minutes

    result = remaining_time
    return result

print(solution())