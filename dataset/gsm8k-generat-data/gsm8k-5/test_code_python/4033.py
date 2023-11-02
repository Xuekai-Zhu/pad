def solution():
    roses_per_dozen = 12  # There are 12 roses in a dozen
    dozens_per_day = 2  # Tom sends 2 dozens of roses per day
    days_per_week = 7  # Tom sends roses for 7 days

    # Calculate the total number of roses Tom sent
    total_roses = dozens_per_day * roses_per_dozen * days_per_week
    result = total_roses
    return result

print(solution())