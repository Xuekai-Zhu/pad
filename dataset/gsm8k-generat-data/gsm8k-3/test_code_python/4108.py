def solution():
    """Justin wanted to watch a movie that came on at 8 pm that night.  His parents agreed as long as he finished his homework and chores before the movie started.  He wouldn't be home until 5 pm because of baseball practice.  He knew dinner would take 45 minutes, and he figured his homework would take 30 minutes to finish.  He needed to clean his room, which would take 30 minutes; then take out the trash, which would take about 5 minutes; and empty the dishwasher,  which would take another 10 minutes.  What was the latest time that Justin could start his chores and homework to be done by 8 pm to watch his movie?"""
    # Calculate the total time Justin needs to finish his chores and homework
    total_time = 45 + 30 + 30 + 5 + 10  # in minutes

    # Subtract the time Justin had before the movie starts
    available_time = (8 * 60) - ((5 * 60) + total_time)  # convert to minutes

    # Calculate the latest time Justin can start his chores and homework
    latest_start_time = (available_time // 60)  # in hours
    if latest_start_time >= 1:
        latest_start_time = '{0}:00 pm'.format(latest_start_time)
    else:
        latest_start_time = '7:{0} pm'.format(available_time)  # if Justin has less than an hour, he can start at 7

    # Display the latest start time
    result = latest_start_time
    return result

print(solution())