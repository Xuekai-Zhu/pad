def solution():
    # Calculate the total distance Scott runs in a week
    weekly_distance = 3*3 + 2*(2*3)  # Scott runs 3 miles every Monday through Wednesday and twice that distance every Thursday and Friday

    # Calculate the total distance Scott runs in a month
    monthly_distance = weekly_distance * 4
    result = monthly_distance
    return result

print(solution())