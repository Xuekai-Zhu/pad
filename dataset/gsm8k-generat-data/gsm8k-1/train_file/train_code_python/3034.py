def solution():
    """Linda makes $10.00 an hour babysitting. There is a $25.00 application fee for each college application she submits. If she is applying to 6 colleges, how many hours will she need to babysit to cover the application fees?"""
    hourly_rate = 10
    num_colleges = 6
    app_fee = 25
    total_fee = num_colleges * app_fee
    hours_needed = total_fee / hourly_rate
    result = hours_needed
    return result

print(solution())