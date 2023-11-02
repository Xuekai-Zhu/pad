def solution():
    # Find the value of the left angle
    right_angle = 60
    left_angle = 2 * right_angle  

    # Find the sum of the left and right angles
    left_right_sum = left_angle + right_angle  

    # Find the value of the top angle
    top_angle = 250 - left_right_sum  
    result = top_angle
    return result

print(solution())