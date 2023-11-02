def solution():
    push_ups_per_break = 5
    number_of_breaks = 2
    seconds_per_break = 8
    seconds_in_a_minute = 60
    push_ups_per_minute = (push_ups_per_break * number_of_breaks) + ((seconds_in_a_minute - (number_of_breaks * seconds_per_break)) * push_ups_per_break / seconds_in_a_minute)
    result = push_ups_per_minute
    return result

print(solution())