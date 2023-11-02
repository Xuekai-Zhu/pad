def solution():
    balloons_start = 50  # Claire starts with 50 balloons
    balloons_lost = 12  # 12 balloons float away while passing one to a little girl
    balloons_given = 9  # Claire gives 9 more balloons away over the next thirty minutes

    # Claire grabs the last 11 from her coworker
    balloons_added = 11  
    balloons_remaining = balloons_start - balloons_lost + balloons_given + balloons_added
    result = balloons_remaining
    return result

print(solution())