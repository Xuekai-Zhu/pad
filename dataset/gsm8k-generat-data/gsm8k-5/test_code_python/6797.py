def solution():
    # Barney's sit-up rate
    barney_rate = 45

    # Carrie's sit-up rate (twice Barney's rate)
    carrie_rate = 2 * barney_rate

    # Jerrie's sit-up rate (5 more than Carrie's rate)
    jerrie_rate = carrie_rate + 5

    # Calculate total number of sit-ups
    barney_total = barney_rate * 1  # 1 minute
    carrie_total = carrie_rate * 2  # 2 minutes
    jerrie_total = jerrie_rate * 3  # 3 minutes

    total_sit_ups = barney_total + carrie_total + jerrie_total
    result = total_sit_ups
    return result

print(solution())