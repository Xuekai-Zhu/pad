def solution():
    total_practice_time = 5 * 60
    monday_practice_time = 2 * 60
    tuesday_practice_time = monday_practice_time / 2
    wednesday_practice_time = tuesday_practice_time + 10
    thursday_practice_time = wednesday_practice_time - 5
    friday_practice_time = total_practice_time - (monday_practice_time + tuesday_practice_time + wednesday_practice_time + thursday_practice_time)
    result = friday_practice_time
    return result

print(solution())