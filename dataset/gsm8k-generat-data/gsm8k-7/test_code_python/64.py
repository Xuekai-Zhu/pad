def solution():
    hourly_rate_main_job = 20
    hourly_rate_second_job = 0.8 * hourly_rate_main_job  # 20% less than main job
    hours_main_job = 30
    hours_second_job = hours_main_job / 2  # half the hours of main job

    # Calculate the total earnings from main job
    earnings_main_job = hourly_rate_main_job * hours_main_job

    # Calculate the total earnings from second job
    earnings_second_job = hourly_rate_second_job * hours_second_job

    # Calculate the total earnings per week
    total_earnings = earnings_main_job + earnings_second_job
    result = total_earnings
    return result

print(solution())