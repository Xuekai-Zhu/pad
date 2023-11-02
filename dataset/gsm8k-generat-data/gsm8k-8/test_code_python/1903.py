def solution():
    # Define the number of days in June and calculate the halfway point
    days_in_june = 30
    halfway_day = days_in_june // 2

    # Calculate the number of video hours uploaded in the first half of June
    hours_first_half = 10 * halfway_day

    # Calculate the remaining days in June and double the number of video hours uploaded
    remaining_days = days_in_june - halfway_day
    doubled_hours_second_half = 2 * 10 * remaining_days

    # Calculate the total number of video hours uploaded in June
    total_hours = hours_first_half + doubled_hours_second_half
    result = total_hours
    return result

print(solution())