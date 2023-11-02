def solution():
    
    initial_firecrackers = 48
    confiscated_firecrackers = 12
    remaining_firecrackers = initial_firecrackers - confiscated_firecrackers
    defective_firecrackers = remaining_firecrackers / 6
    good_firecrackers = remaining_firecrackers - defective_firecrackers
    set_off_firecrackers = good_firecrackers / 2
    result = set_off_firecrackers
    return result

print(solution())