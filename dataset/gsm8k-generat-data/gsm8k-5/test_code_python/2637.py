def solution():
    dresses_needed = 5  # There are 5 bridesmaids in the wedding
    time_per_dress = 12  # Sheena can sew one dress in 12 hours
    total_time_needed = dresses_needed * time_per_dress  # Sheena needs to sew all the dresses

    sewing_time_per_week = 4  # Sheena sews for 4 hours each week
    weeks_needed = total_time_needed / sewing_time_per_week

    result = weeks_needed
    return result

print(solution())