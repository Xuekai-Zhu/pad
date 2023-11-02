def solution():
    """The Parker family needs to leave the house by 5 pm for a dinner party. Mrs. Parker was waiting to get into the bathroom at 2:30 pm. Her oldest daughter used the bathroom for 45 minutes and her youngest daughter used the bathroom for another 30 minutes. Then her husband used it for 20 minutes. How much time will Mrs. Parker have to use the bathroom to leave on time?"""
    dinner_time = 17.0
    current_time = 14.5
    used_time = 0.0

    # oldest daughter used the bathroom
    used_time += 0.75
    # youngest daughter used the bathroom
    used_time += 0.5
    # husband used the bathroom
    used_time += 0.33333

    available_time = dinner_time - current_time - used_time

    result = available_time
    return result

print(solution())