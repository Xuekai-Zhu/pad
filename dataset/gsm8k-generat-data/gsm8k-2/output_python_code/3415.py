def solution():
    """September's temperature fluctuated severely in 1 week. They started off with 40 degrees on Sunday then hit 50 on Monday, 65 on Tuesday, 36 on Wednesday, 82 on Thursday, 72 on Friday and ended the week at 26 on Saturday. What was the average temperature for that week?"""
    temperatures = [40, 50, 65, 36, 82, 72, 26]
    total_temp = sum(temperatures)
    num_temp = len(temperatures)
    average_temp = total_temp / num_temp
    result = average_temp
    return result

print(solution())