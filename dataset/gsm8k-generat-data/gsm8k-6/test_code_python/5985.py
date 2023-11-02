def solution():
    # Calculate the total hours of sleep in the four day period
    total_sleep = 6 + (6+2) + ((6+2)/2) + ((6+2)/2)*3  # Billy sleeps 6 hours the first night, then 2 hours more the next night, then half the previous amount the third night, then triple the previous amount the final night
    result = total_sleep
    return result

print(solution())