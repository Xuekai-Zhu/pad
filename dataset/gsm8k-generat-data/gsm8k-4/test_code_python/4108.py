def solution():
    """Justin wanted to watch a movie that came on at 8 pm that night. His parents agreed as long as he finished his homework and chores before the movie started. He wouldn't be home until 5 pm because of baseball practice. He knew dinner would take 45 minutes, and he figured his homework would take 30 minutes to finish. He needed to clean his room, which would take 30 minutes; then take out the trash, which would take about 5 minutes; and empty the dishwasher, which would take another 10 minutes. What was the latest time that Justin could start his chores and homework to be done by 8 pm to watch his movie?"""
    
    # total time Justin has before the movie starts
    total_time = 3 * 60   #3 hours

    # subtract the time Justin will spend at baseball practice
    total_time -= 2     #2 hours

    # subtract the time Justin will spend for dinner
    total_time -= 45     #45 minutes

    # subtract the time Justin will spend for cleaning his room and other chores
    total_time -= 30+5+10    #30 minutes for cleaning room, 5 minutes for taking out trash, 10 minutes for emptying the dishwasher

    # subtract the time Justin will spend for doing his homework
    total_time -= 30    #30 minutes

    # calculate the latest time that Justin could start his chores and homework
    latest_start_time = (8 * 60) - total_time    #8 pm in minutes is 480

    # format the result to a string in "HH:MM" format
    result = "{:02d}:{:02d}".format(latest_start_time // 60, latest_start_time % 60)
    return result

print(solution())