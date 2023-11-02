def solution():
    monday_time = 2
    tuesday_time = 4
    wednesday_time = 3
    thursday_time = 4
    old_average = 3

    # Calculate the total time Osborn spent getting dressed from Monday to Thursday
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time

    # Calculate the time Osborn needs to spend getting dressed on Friday to tie his old average
    friday_time = (old_average * 5) - total_time

    result = friday_time
    return result

print(solution())