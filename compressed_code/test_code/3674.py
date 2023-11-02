def solution():
    
    first_set_size = 50
    first_set_broken_perc = 0.1
    second_set_size = 60
    second_set_broken_perc = 0.2
    total_broken = first_set_size * first_set_broken_perc + second_set_size * second_set_broken_perc
    result = total_broken
    return result

print(solution())