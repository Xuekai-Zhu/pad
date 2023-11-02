def solution():
    netflix_hours = 10
    netflix_data_per_hour = 1/5 # 0.2 TB per hour
    netflix_data_per_day = netflix_hours * netflix_data_per_hour # 2 TB per day
    usb_capacity = 500 # GB
    if netflix_data_per_day <= usb_capacity*1000:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())