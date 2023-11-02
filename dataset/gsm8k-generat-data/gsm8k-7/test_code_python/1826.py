def solution():
    monday_pushups = 5
    tuesday_pushups = 7
    wednesday_pushups = 2 * tuesday_pushups
    total_pushups_so_far = monday_pushups + tuesday_pushups + wednesday_pushups

    thursday_pushups = total_pushups_so_far / 2
    friday_pushups = total_pushups_so_far + thursday_pushups

    result = friday_pushups
    return result

print(solution())