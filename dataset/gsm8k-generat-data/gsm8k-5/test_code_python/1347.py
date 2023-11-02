def solution():
    cabinets_over_one_counter = 3  # Jeff has 3 cabinets over one counter
    cabinets_over_three_counters = 2 * cabinets_over_one_counter  # Jeff installs twice as many cabinets over 3 different counters
    total_additional_cabinets = cabinets_over_three_counters * 3  # Jeff installs cabinets over 3 counters
    total_cabinets = cabinets_over_one_counter + total_additional_cabinets + 5  # Jeff installs 5 more cabinets

    result = total_cabinets
    return result

print(solution())