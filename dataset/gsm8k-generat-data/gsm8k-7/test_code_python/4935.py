def solution():
    cal_burned_per_day = 2500
    cal_per_lb = 3500
    lbs_to_lose = 5
    cal_per_day_eaten = 2000

    # Calculate the total calories needed to burn to lose the desired amount of weight
    total_cal_burned = lbs_to_lose * cal_per_lb

    # Calculate the number of days needed to burn off the desired amount of weight
    num_days = total_cal_burned / (cal_burned_per_day - cal_per_day_eaten)
    result = num_days
    return result

print(solution())