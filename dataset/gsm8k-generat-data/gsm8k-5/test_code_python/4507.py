def solution():
    naps_per_week = 3  # John takes 3 naps per week
    nap_length = 2  # Each nap is 2 hours long
    days = 70  # John wants to know how many hours of naps he takes in 70 days

    # Calculate the total number of hours of naps John takes in 70 days
    total_nap_hours = naps_per_week * nap_length * (days // 7)

    result = total_nap_hours
    return result

print(solution())