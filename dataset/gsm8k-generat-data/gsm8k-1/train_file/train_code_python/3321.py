def solution():
    """Tony goes on 5 rollercoasters while he is at the park. The first went 50 miles per hour. The second went 62 miles per hour. The third when 73 miles per hour. The fourth when 70 miles per hour. His average speed during the day was 59 miles per hour. How fast was the fifth coaster?"""
    total_speed = 59 * 5 #Total speed for all 5 rollercoasters
    speed_of_5th_rollercoaster = total_speed - (50 + 62 + 73 + 70) #Subtracting previous 4 speeds from total
    result = speed_of_5th_rollercoaster
    return result

print(solution())