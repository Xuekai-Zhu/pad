def solution():
    samantha_sleeps = 8
    sister_sleeps = 2.5 * samantha_sleeps
    father_sleeps_per_sister_hour = 0.5 # he sleeps 30 minutes for every hour the baby sleeps
    num_days = 7

    # Calculate the total number of hours Samantha's sister will sleep in a week
    total_sister_sleeps = sister_sleeps * num_days

    # Calculate the total number of hours Samantha's father will sleep in a week
    total_father_sleeps = total_sister_sleeps * father_sleeps_per_sister_hour
    result = total_father_sleeps
    return result

print(solution())