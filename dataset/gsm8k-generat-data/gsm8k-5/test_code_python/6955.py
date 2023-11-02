def solution():
    total_practice_time = 5 * 60  # Carlo needs to practice for 5 hours which is equal to 300 minutes
    thursday_practice_time = 50  # Carlo practiced for 50 minutes on Thursday
    wednesday_practice_time = thursday_practice_time + 5  # Carlo practiced 5 minutes more on Wednesday than on Thursday
    tuesday_practice_time = wednesday_practice_time - 10  # Carlo practiced 10 minutes less on Tuesday than on Wednesday
    monday_practice_time = 2 * tuesday_practice_time  # Carlo practiced twice as long on Monday as on Tuesday

    # Calculate the total practice time so far
    total_practice_time_so_far = monday_practice_time + tuesday_practice_time + wednesday_practice_time + thursday_practice_time

    # Calculate the remaining practice time
    remaining_practice_time = total_practice_time - total_practice_time_so_far

    # Calculate Carlo's required practice time on Friday
    friday_practice_time = remaining_practice_time

    result = friday_practice_time
    return result

print(solution())