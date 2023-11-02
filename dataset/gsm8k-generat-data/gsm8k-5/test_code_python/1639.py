def solution():
    total_balloons = 50  # Andy stopped blowing up balloons when there were 50 balloons
    balloons_already_blown = 12  # Ashley already blew up 12 balloons
    balloons_blown_by_andy = total_balloons - balloons_already_blown  # Andy blew up the remaining balloons

    time_in_minutes = balloons_blown_by_andy * 5 / 2  # Andy blew up 2 balloons every 5 minutes
    result = time_in_minutes
    return result

print(solution())