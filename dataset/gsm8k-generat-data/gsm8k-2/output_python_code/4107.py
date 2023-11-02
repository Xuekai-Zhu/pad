def solution():
    """Justin wanted to watch a movie that came on at 8 pm that night. His parents agreed as long as he finished his homework and chores before the movie started. He wouldn't be home until 5 pm because of baseball practice. He knew dinner would take 45 minutes, and he figured his homework would take 30 minutes to finish. He needed to clean his room, which would take 30 minutes; then take out the trash, which would take about 5 minutes; and empty the dishwasher, which would take another 10 minutes. What was the latest time that Justin could start his chores and homework to be done by 8 pm to watch his movie?"""
    time_available = 3 * 60  # in minutes
    time_spent = (5 + 45 + 30 + 30 + 5 + 10)  # in minutes
    time_left = time_available - time_spent
    latest_start_time = 8 * 60 - time_left
    result = latest_start_time
    return result

print(solution())