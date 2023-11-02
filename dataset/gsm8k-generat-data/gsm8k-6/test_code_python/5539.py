def solution():
    # Calculate the total time Monica spent studying
    wednesday_time = 2
    thursday_time = 3 * wednesday_time
    friday_time = thursday_time / 2
    weekend_time = (wednesday_time + thursday_time + friday_time) * 2
    total_time = wednesday_time + thursday_time + friday_time + weekend_time
    result = total_time
    return result

print(solution())