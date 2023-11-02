def solution():
    days_of_protest = 30
    number_of_cities = 21
    arrests_per_day = 10
    days_in_jail_before_trial = 4
    average_sentence = 2.5
    total_jail_time = (days_of_protest * number_of_cities * arrests_per_day * days_in_jail_before_trial) + ((days_of_protest * number_of_cities * arrests_per_day) / 2)
    result = total_jail_time
    return result

print(solution())