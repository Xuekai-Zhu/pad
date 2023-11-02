def solution():
    
    snails_on_first_day = 3
    snails_on_previous_day = snails_on_first_day
    total_snails = snails_on_first_day
    for i in range(1, 5):
        snails_on_current_day = snails_on_previous_day + 2
        total_snails += snails_on_current_day
        snails_on_previous_day = snails_on_current_day

    result = total_snails
    return result

print(solution())