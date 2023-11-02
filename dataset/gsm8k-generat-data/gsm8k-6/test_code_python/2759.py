def solution():
    # Calculate the time spent biking, taking the bus, and getting a ride from a friend
    time_biking = 30  # minutes
    time_bus = (30 + 10) * 3  # 10 minutes longer than biking, multiplied by 3 days a week
    time_friend = (2/3) * time_biking  # two-thirds less of biking time, multiplied by once a week

    # Calculate the total time spent commuting to work every week
    total_time = time_biking + time_bus + time_friend
    result = total_time
    return result

print(solution())