def solution():
    """The Parker family needs to leave the house by 5 pm for a dinner party. Mrs. Parker was waiting to get into the bathroom at 2:30 pm. Her oldest daughter used the bathroom for 45 minutes and her youngest daughter used the bathroom for another 30 minutes. Then her husband used it for 20 minutes. How much time will Mrs. Parker have to use the bathroom to leave on time?"""
    total_bathroom_time = 45 + 30 + 20
    current_time = 14 + 30/60
    time_left = 17 - current_time - total_bathroom_time/60
    result = time_left * 60
    return result

print(solution())