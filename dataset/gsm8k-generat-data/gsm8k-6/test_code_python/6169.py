def solution():
    # Calculate how far Tomas can run each month leading up to the marathon
    monthly_distance = [3]  # start with the first month
    for i in range(1, 12):  # assume he trains for 12 months leading up to the marathon
        current_distance = monthly_distance[i-1] * 2  # he can run twice as far as the previous month
        monthly_distance.append(current_distance)

    # Calculate the total number of months needed to reach 26.3 miles
    total_distance = 0
    month_count = 0
    while total_distance < 26.3:
        total_distance += monthly_distance[month_count]
        month_count += 1

    result = month_count
    return result

print(solution())