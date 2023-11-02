def solution():
    # Calculate the number of visitors on Tuesday
    visitors_on_tuesday = 2 * 50

    # Calculate the number of visitors on the remaining days of the week
    remaining_days = 5
    average_visitors = 20
    visitors_on_remaining_days = remaining_days * average_visitors

    # Calculate the total number of visitors for the week
    total_visitors = 50 + visitors_on_tuesday + visitors_on_remaining_days
    result = total_visitors
    return result

print(solution())