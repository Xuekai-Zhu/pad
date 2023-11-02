def solution():
    # Calculate the number of balloons each person can inflate in 30 minutes
    balloons_Mary = 10 * 30  # Mary inflates 10 balloons per minute
    balloons_Jess = 7 * 30  # Jess inflates 7 balloons per minute
    balloons_Christina = 4 * 15 + 4 * 15  # Christina came 15 minutes late and inflates 4 balloons per minute, so she can inflate 60 balloons in the remaining time

    # Calculate the total number of balloons that can be inflated in 30 minutes
    total_balloons = balloons_Mary + balloons_Jess + balloons_Christina
    result = total_balloons
    return result

print(solution())