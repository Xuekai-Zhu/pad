def solution():
    total_firecrackers = 48
    confiscated_firecrackers = 12
    remaining_firecrackers = total_firecrackers - confiscated_firecrackers
    defective_firecrackers = remaining_firecrackers / 6
    good_firecrackers = remaining_firecrackers - defective_firecrackers
    num_set_off = good_firecrackers / 2
    result = num_set_off
    return result

print(solution())