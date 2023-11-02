def solution():
    # Calculate the total number of balloons bought
    total_balloons = 5 * 20 + 4 * 30  # 5 bags of round balloons with 20 balloons in each bag and 4 bags of long balloons with 30 balloons in each bag

    # Calculate the number of balloons that burst
    burst_balloons = 5

    # Calculate the number of balloons left
    balloons_left = total_balloons - burst_balloons
    
    result = balloons_left
    return result

print(solution())