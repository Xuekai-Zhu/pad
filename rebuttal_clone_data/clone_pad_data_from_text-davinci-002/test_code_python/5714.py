def solution():
    jalapeno_peppers_per_sandwich = 4
    sandwiches_per_minute = 1/5
    minutes_in_an_hour = 60
    hours_in_a_day = 8
    total_sandwiches = sandwiches_per_minute * minutes_in_an_hour * hours_in_a_day
    total_jalapeno_peppers = total_sandwiches * jalapeno_peppers_per_sandwich
    result = total_jalapeno_peppers
    
    return result

print(solution())