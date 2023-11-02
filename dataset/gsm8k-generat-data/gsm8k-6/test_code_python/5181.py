def solution():
    # Calculate the distance Jenny travels in 30 minutes
    distance_jenny = (15 / 60) * 30   # 15 miles per hour = (15/60) miles per minute, she travels for half an hour
    # Calculate the time it takes Anna to catch up with Jenny
    time_anna = distance_jenny / (45 / 60)   # 45 miles per hour = (45/60) miles per minute
    # Convert the time into minutes
    time_anna_minutes = time_anna * 60

    result = time_anna_minutes
    return result

print(solution())