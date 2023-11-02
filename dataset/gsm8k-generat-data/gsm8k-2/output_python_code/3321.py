def solution():
    """Tony goes on 5 rollercoasters while he is at the park. The first went 50 miles per hour. The second went 62 miles per hour. The third when 73 miles per hour. The fourth when 70 miles per hour. His average speed during the day was 59 miles per hour. How fast was the fifth coaster?"""
    total_speed = 59 * 5
    speed_of_first_4 = 50 + 62 + 73 + 70
    speed_of_fifth = total_speed - speed_of_first_4
    result = speed_of_fifth
    return result

print(solution())