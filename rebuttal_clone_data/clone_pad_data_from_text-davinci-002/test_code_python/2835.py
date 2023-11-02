def solution():
    surfers_first_day = 1500
    surfers_second_day = surfers_first_day + 600
    surfers_third_day = surfers_first_day - (surfers_first_day / 5)
    average_surfers = (surfers_first_day + surfers_second_day + surfers_third_day) / 3
    result = average_surfers
    return result

print(solution())