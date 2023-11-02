def solution():
    pay_per_weed = 0.05
    total_pay_per_hour = 10.0
    seconds_in_hour = 3600

    # Calculate the number of weeds Heather can pick in an hour
    num_weeds_per_hour = total_pay_per_hour / pay_per_weed

    # Calculate the number of seconds it takes to pick one weed
    seconds_per_weed = seconds_in_hour / num_weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())