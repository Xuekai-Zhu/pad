def solution():
    # Calculate the total time spent on the phone per month
    total_time_min = 60 * 1 * 50 * 4  # 1 hour per call, 50 customers per week, 4 weeks in a month
    total_time_sec = total_time_min * 60  # convert to seconds

    # Calculate the phone bill for the month
    phone_bill = total_time_sec * 0.05  # 5 cents per minute
    result = phone_bill
    return result

print(solution())